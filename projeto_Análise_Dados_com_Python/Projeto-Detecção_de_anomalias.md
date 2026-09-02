# Projeto - Detecção de anomalias em transações Python

> O principal foco é a questão do desbalanceamento dos dados, tendo que balancear para que possamos obter um modelo de aprendizado consistênte

Será utilizado o Pandas
criar um dataframe e utilizar um df.head() para se analizar os primeiros dados.
Limpar dados
Normalizar os dados
Criar uma classificação desbalanceada
Acurácia - porcentagem de acertos do modelo
Utilizar o Recall
train_test_split (importante para separar a parte de teste e a parte de treino)
random_state_42 
### Feature engeneering
> Criamos variáveis que ajudam o modelo

**importar o numpy**
criar uma variável de compressão logarítmica (log1p - função do numpy)
sidekick learning (sklearn.preprocessing - StandardScaler)
Separar dados em X e Y

* Logistic Regression
* ROC Curve
* Precision-Recall Curve

> Balanceamento de dados com o Oversampling ou Undersampling - Para saber qual o melhor modelo de balanceamento, deve-se testar ambas

### Random forest classifier
>Baseado em árvore de deciões, tendendo a ser mais preciso<

### XGBoost
>Algoritmo baseado em boosts, treinando vários modelos para que se corrijam entre si<


Desafio:
Interpretar a importância das variáveis
Ajuste de hiperparâmetros: testa-se várias combinações para testar o modelo.

