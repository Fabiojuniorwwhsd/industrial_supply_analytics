"""
ETL Supply Analytics

Lê bases fictícias de cenário industrial, integra os arquivos e gera uma base analítica para dashboard.
Todos os dados são sintéticos.
"""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
EXPORTS = ROOT / "exports"

def main():
    pedidos = pd.read_csv(RAW / "pedidos_compra.csv")
    fornecedores = pd.read_csv(RAW / "fornecedores.csv")
    entregas = pd.read_csv(RAW / "entregas.csv")
    estoque = pd.read_csv(RAW / "estoque.csv")
    avarias = pd.read_csv(RAW / "avarias.csv")

    base = pedidos.merge(fornecedores, on="id_fornecedor", how="left")                  .merge(estoque, on="id_material", how="left")                  .merge(entregas, on="id_pedido", how="left")

    avarias_agg = avarias.groupby("id_pedido", as_index=False).agg(
        quantidade_avariada=("quantidade_avariada", "sum"),
        qtd_registros_avaria=("id_avaria", "count")
    )
    base = base.merge(avarias_agg, on="id_pedido", how="left")
    base[["quantidade_avariada", "qtd_registros_avaria"]] = base[["quantidade_avariada", "qtd_registros_avaria"]].fillna(0).astype(int)

    for col in ["data_pedido", "data_prevista_entrega", "data_entrega"]:
        base[col] = pd.to_datetime(base[col], errors="coerce")

    base["lead_time_dias"] = (base["data_entrega"] - base["data_pedido"]).dt.days
    base["dias_atraso"] = (base["data_entrega"] - base["data_prevista_entrega"]).dt.days
    base["pedido_atrasado"] = np.where(base["dias_atraso"] > 0, 1, 0)
    base["estoque_critico"] = np.where(base["estoque_atual"] < base["estoque_minimo"], 1, 0)
    base["mes_pedido"] = base["data_pedido"].dt.to_period("M").astype(str)

    for col in ["data_pedido", "data_prevista_entrega", "data_entrega"]:
        base[col] = base[col].dt.strftime("%Y-%m-%d").fillna("")

    PROCESSED.mkdir(parents=True, exist_ok=True)
    EXPORTS.mkdir(parents=True, exist_ok=True)
    base.to_csv(PROCESSED / "base_analitica_supply.csv", index=False, encoding="utf-8-sig")

    kpis = pd.DataFrame([
        {"indicador":"Total de pedidos", "valor":len(base), "unidade":"pedidos"},
        {"indicador":"Pedidos entregues", "valor":int(base["data_entrega"].replace("", np.nan).notna().sum()), "unidade":"pedidos"},
        {"indicador":"OTIF", "valor":round(base["otif"].fillna(0).astype(float).mean()*100, 2), "unidade":"%"},
        {"indicador":"Pedidos em atraso", "valor":round(base["pedido_atrasado"].mean()*100, 2), "unidade":"%"},
        {"indicador":"Materiais em estoque crítico", "valor":round(base.drop_duplicates("id_material")["estoque_critico"].mean()*100, 2), "unidade":"%"},
        {"indicador":"Registros de avaria", "valor":int(base["qtd_registros_avaria"].sum()), "unidade":"ocorrências"}
    ])
    kpis.to_csv(EXPORTS / "kpis_resumo.csv", index=False, encoding="utf-8-sig")
    print("ETL concluído com sucesso.")

if __name__ == "__main__":
    main()
