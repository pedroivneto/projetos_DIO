# Detecção de Anomalias em Transações de Cartão de Crédito

> O objetivo deste projeto é demonstrar, na prática, o pipeline completo de ciência de dados — da ingestão via API ao treinamento de algoritmos de Machine Learning —, focando no desempenho e comparativo de modelos diante de dados desbalanceados.

---

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python
* **Coleta de Dados:** `requests` (Integração com API)
* **Análise e ML:** Pandas, NumPy, Scikit-Learn, XGBoost, Matplotlib, Seaborn

## 🔄 Fluxo do Projeto
1. **Coleta de Dados:** Obtenção dos dados de transações consumindo uma API REST com a biblioteca `requests`.
2. **Análise Exploratória & Tratamento:** Limpeza, padronização e tratamento do desbalanceamento das classes.
3. **Modelagem & Avaliação:** Treinamento e validação dos algoritmos de classificação.

## 🤖 Modelos Avaliados
* Regressão Logística
* Árvore de Decisão (*Decision Tree*)
* Floresta Aleatória (*Random Forest*)
* XGBoost

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
