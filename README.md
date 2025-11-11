## 🌞 Solar Rank

## Projeto desenvolvido como parte da disciplina Big Data, ministrada pelo Professor Vinícius, no período 2025.2
### Participantes: Paulo Terror, Danielle Carvalho, Douglas Lira, Geovanna Melo e Lorenzo Lopes.

## 
Análise de eficiência da geração solar municipal com foco em priorização de investimentos, utilizando Pandas para processamento de dados, Seaborn para visualização e Apache Prefect para orquestração dos fluxos de análise.

## 📘 Descrição do Projeto

O Solar Rank tem como objetivo processar e analisar dados de geração solar municipal, criando uma métrica de eficiência baseada na relação entre a geração (MWh) e a capacidade instalada (kW).
A partir dessa métrica, as cidades são ranqueadas e classificadas conforme sua eficiência, permitindo identificar quais devem ser prioritárias para investimento em energia solar.

## ⚙️ Tecnologias Utilizadas

🐍 Python 3.10+ — linguagem principal do projeto

🧮 Pandas — tratamento, cálculo e manipulação dos dados

📊 Seaborn — criação de gráficos e visualizações de desempenho

🧠 Prefect — orquestração dos fluxos de análise

📁 CSV — formato da base de dados de entrada (energia_solar.csv)

## 📈 Métricas Calculadas

Eficiência = geracao_solar_mwh / capacidade_kw

Classificação por Regra:

Eficiência > 0.12 → Prioritária

Caso contrário → Não prioritária

## 📊 Resultados Esperados

Geração de ranking das 3 cidades mais eficientes

Visualização gráfica das cidades com melhor desempenho

Tabela consolidada com classificação de priorização

## 🚀 Execução

Instale as dependências:

pip install pandas seaborn prefect

Visualize os resultados gerados na pasta /output ou diretamente no notebook.
