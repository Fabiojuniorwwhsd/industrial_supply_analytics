# Industrial Supply Analytics — KPIs de Suprimentos, Estoque e Entregas

## Descrição

Este projeto simula um cenário de análise de dados em ambiente industrial, utilizando bases fictícias de pedidos de compra, fornecedores, entregas, estoque e avarias.

O objetivo é demonstrar um fluxo analítico completo, desde a preparação dos dados até a construção de indicadores para apoio à tomada de decisão orientada por dados.

> **Observação importante:** todos os dados deste projeto são sintéticos e foram criados exclusivamente para fins educacionais e de portfólio. Nenhuma informação real, sensível, confidencial ou protegida por LGPD foi utilizada.

## Problema analisado

O projeto busca responder perguntas como:

- Quais fornecedores apresentam maior volume de atrasos?
- Qual é o percentual de entregas realizadas no prazo e na quantidade correta?
- Quais materiais estão em situação de estoque crítico?
- Quais pedidos apresentam divergência entre quantidade solicitada e quantidade recebida?
- Quais categorias concentram mais avarias?
- Como os indicadores evoluem ao longo dos meses?

## Fontes de dados

As bases utilizadas são fictícias e simulam dados de:

- Pedidos de compra
- Fornecedores
- Entregas
- Estoque
- Avarias

## Ferramentas utilizadas

- Python
- Pandas
- SQL
- Excel/Google Sheets
- Power Query
- Power BI ou Looker Studio
- GitHub

## Estrutura do repositório

```text
industrial-supply-analytics/
├── data/raw/
├── data/processed/
├── notebooks/
├── scripts/
├── exports/
├── dashboard/
└── docs/
```

## Etapas do projeto

1. Criação de bases fictícias para simular um cenário industrial.
2. Leitura dos arquivos CSV brutos.
3. Tratamento de dados nulos, duplicados e inconsistentes.
4. Padronização de datas, categorias, status e chaves.
5. Integração das bases de pedidos, fornecedores, entregas, estoque e avarias.
6. Criação da base analítica final.
7. Construção de indicadores operacionais.
8. Preparação dos dados para dashboard em Power BI ou Looker Studio.

## Indicadores desenvolvidos

- OTIF
- Pedidos em atraso
- Tempo médio de entrega
- Divergência de quantidade
- Estoque crítico
- Avarias por fornecedor
- Ranking de fornecedores críticos
- Evolução mensal de entregas

## Como executar

```bash
pip install -r requirements.txt
python scripts/etl_supply.py
```

A base final será gerada em:

```text
data/processed/base_analitica_supply.csv
```

## Observação sobre confidencialidade

Este projeto é baseado em um cenário fictício e utiliza apenas dados sintéticos. Nenhuma informação real, sensível, confidencial ou protegida por LGPD foi utilizada.
