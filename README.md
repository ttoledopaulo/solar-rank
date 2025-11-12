# 🌞 Solar Rank

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4B8BBE.svg?logo=plotly)](https://seaborn.pydata.org/)
[![Prefect](https://img.shields.io/badge/Prefect-Orchestration-18BFFF.svg?logo=prefect)](https://www.prefect.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
---

### 🏫 Projeto desenvolvido como **forma de avaliação** da disciplina de **Big Data**, ministrada pelo **Professor Vinícius**, no período **2025.2**

---

## 🧠 Visão Geral

Análise de eficiência da geração solar municipal com foco em **priorização de investimentos**, utilizando **Pandas** para processamento de dados, **Seaborn** para visualização e **Prefect** para **orquestração de pipeline**.

---

---

## 📘 Descrição do Projeto

O **Solar Rank** tem como objetivo processar e analisar dados de geração solar municipal, criando uma **métrica de eficiência** baseada na relação entre a **geração (MWh)** e a **capacidade instalada (kW)**.  
A partir dessa métrica, as cidades são **ranqueadas e classificadas** conforme sua eficiência, permitindo identificar quais devem ser **prioritárias para investimento em energia solar**.

---

## 📈 Métricas Calculadas

- **Eficiência** = `geracao_solar_mwh / capacidade_kw`  
- **Classificação por Regra:**  
  - Eficiência > 0.12 → `Prioritária`  
  - Caso contrário → `Não prioritária`

---

## 🚀 Como Usar

### 📋 Pré-requisitos

Certifique-se de ter o Python 3.10+ instalado e instale as dependências:
```bash
pip install -r requirements.txt
```

### ▶️ Executando o Projeto

#### 1️⃣ **Executar o Pipeline de Dados**
```bash
python -m src.orchestration.pipeline
```

#### 2️⃣ **Gerar Visualizações**
```bash
python -m src.graficos
```