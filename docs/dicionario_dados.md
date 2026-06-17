# Dicionário de Dados

## Arquivos

- `fornecedores.csv`: fornecedores sintéticos, UF, categoria, criticidade e SLA.
- `estoque.csv`: materiais sintéticos, categoria, estoque mínimo e estoque atual.
- `pedidos_compra.csv`: pedidos fictícios, quantidade, valor, previsão de entrega e status.
- `entregas.csv`: entregas fictícias, quantidade recebida, divergência e OTIF.
- `avarias.csv`: registros fictícios de avarias por pedido.
- `base_analitica_supply.csv`: base integrada para análise e dashboard.

## Campos principais

| Campo | Descrição |
|---|---|
| id_pedido | Identificador sintético do pedido |
| id_fornecedor | Identificador sintético do fornecedor |
| id_material | Identificador sintético do material |
| quantidade_pedida | Quantidade solicitada no pedido |
| quantidade_recebida | Quantidade recebida na entrega |
| divergencia_quantidade | Diferença entre recebido e pedido |
| entregue_no_prazo | Indica se a entrega ocorreu no prazo |
| entrega_completa | Indica se a entrega foi completa |
| otif | Entrega no prazo e na quantidade correta |
| lead_time_dias | Tempo entre pedido e entrega |
| dias_atraso | Dias de atraso em relação à data prevista |
| estoque_critico | Indica material abaixo do estoque mínimo |
