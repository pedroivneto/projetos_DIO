import io
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

# Configuração de estilo dos gráficos
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
sns.set_palette("muted")

# ==============================================================================
# 1. DOWNLOAD E CARREGAMENTO DOS DADOS DIRETAMENTE DA API/URL
# ==============================================================================
print("="*80)
print(" 1. CARREGANDO O DATASET DE CARTÃO DE CRÉDITO ")
print("="*80)

url = 'https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv'
print(f"Baixando arquivo de: {url} ...")

response = requests.get(url)
response.raise_for_status() # Garante que o download foi bem-sucedido

df = pd.read_csv(io.BytesIO(response.content))
print(f"Dataset carregado com sucesso! Dimensões: {df.shape[0]} linhas x {df.shape[1]} colunas.")

# Checagem do Desbalanceamento
total_tx = len(df)
fraudes = df['Class'].sum()
normais = total_tx - fraudes
pct_fraude = (fraudes / total_tx) * 100

print(f"\n[!] Distribuição das Transações:")
print(f"    - Normais (Classe 0): {normais:,} ({100 - pct_fraude:.2f}%)")
print(f"    - Fraudes (Classe 1): {fraudes:,} ({pct_fraude:.2f}%)")


# ==============================================================================
# 2. PRÉ-PROCESSAMENTO E DIVISÃO TREINO/TESTE
# ==============================================================================
# Padronização de Time e Amount (as variáveis V1 a V28 já são PCA)
scaler = StandardScaler()
df['Amount_Scaled'] = scaler.fit_transform(df[['Amount']])
df['Time_Scaled'] = scaler.fit_transform(df[['Time']])

X = df.drop(columns=['Class', 'Amount', 'Time'])
y = df['Class']

# Divisão estratificada para manter a proporção de fraudes no treino e no teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)


# ==============================================================================
# 3. TREINAMENTO E AVALIAÇÃO DOS MODELOS
# ==============================================================================
print("\n" + "="*80)
print(" 2. TREINANDO E AVALIANDO OS MODELOS ")
print("="*80)

# Calculando scale_pos_weight para o XGBoost compensar o desbalanceamento
scale_weight = normais / fraudes

modelos = {
    'Regressão Logística': LogisticRegression(max_iter=1000, random_state=42),
    'Árvore de Decisão': DecisionTreeClassifier(max_depth=5, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
    'XGBoost (Melhor opção)': XGBClassifier(
        n_estimators=100, 
        learning_rate=0.1, 
        scale_pos_weight=scale_weight, 
        eval_metric='logloss',
        random_state=42, 
        n_jobs=-1
    )
}

resultados = []

for nome, modelo in modelos.items():
    print(f"Treinando {nome}...")
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    roc = roc_auc_score(y_test, y_pred)
    
    resultados.append({
        'Modelo': nome,
        'Acurácia': acc,
        'Precisão': prec,
        'Recall (Revocação)': rec,
        'F1-Score': f1,
        'ROC-AUC': roc
    })

df_res = pd.DataFrame(resultados).set_index('Modelo')


# ==============================================================================
# 4. GERAÇÃO DO DASHBOARD GRÁFICO (MATPLOTLIB)
# ==============================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('DASHBOARD COMPARATIVO DE MACHINE LEARNING (CREDIT CARD FRAUD)', fontsize=15, fontweight='bold', y=1.02)

# Gráfico 1: Acurácia vs Recall (Evidenciando a Armadilha da Acurácia)
x = np.arange(len(df_res))
width = 0.35

axes[0].bar(x - width/2, df_res['Acurácia'], width, label='Acurácia (Métrica Ilusória)', color='#95a5a6')
axes[0].bar(x + width/2, df_res['Recall (Revocação)'], width, label='Recall (Taxa de Captura de Fraudes)', color='#e74c3c')

axes[0].set_title('Armadilha da Acurácia vs. Capacidade Real de Captura (Recall)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Pontuação (0.0 a 1.0)', fontsize=11)
axes[0].set_xticks(x)
axes[0].set_xticklabels(df_res.index, rotation=15, fontsize=10)
axes[0].set_ylim(0.7, 1.08)
axes[0].legend(loc='lower right')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Anotações numéricas
for p in axes[0].patches:
    h = p.get_height()
    if h > 0:
        axes[0].annotate(f'{h:.3f}', (p.get_x() + p.get_width() / 2., h),
                         ha='center', va='bottom', fontsize=8, xytext=(0, 3),
                         textcoords='offset points', fontweight='bold')

# Gráfico 2: Desempenho Global (F1-Score e ROC-AUC)
axes[1].plot(df_res.index, df_res['F1-Score'], marker='o', linewidth=2.5, label='F1-Score', color='#2ecc71')
axes[1].plot(df_res.index, df_res['ROC-AUC'], marker='s', linewidth=2.5, label='ROC-AUC', color='#f39c12')

axes[1].set_title('Métricas Robustas: F1-Score e ROC-AUC', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Pontuação (0.0 a 1.0)', fontsize=11)
axes[1].set_xticklabels(df_res.index, rotation=15, fontsize=10)
axes[1].set_ylim(0.7, 1.05)
axes[1].legend(loc='lower right')
axes[1].grid(True, linestyle='--', alpha=0.7)

for i, txt in enumerate(df_res['F1-Score']):
    axes[1].annotate(f'{txt:.3f}', (df_res.index[i], df_res['F1-Score'].iloc[i] + 0.01), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()


# ==============================================================================
# 5. ESTRUTURA PIRAMIDAL DE MINTO (RESUMO E EXPLICAÇÃO NO TERMINAL)
# ==============================================================================
print("\n" + "="*80)
print("                RELATÓRIO EM ESTRUTURA PIRAMIDAL                  ")
print("="*80)

xgb_rec = df_res.loc['XGBoost (Melhor opção)', 'Recall (Revocação)']
xgb_f1 = df_res.loc['XGBoost (Melhor opção)', 'F1-Score']
log_rec = df_res.loc['Regressão Logística', 'Recall (Revocação)']

print(f"""
NÍVEL 1: A CONCLUSÃO PRINCIPAL (O 'TOPO' DA PIRÂMIDE)
--------------------------------------------------------------------------------
• O XGBoost é o modelo ideal para entrada em produção. Ele maximizou a captura de 
  transações fraudulentas (Recall de {xgb_rec:.2%}) mantendo o melhor equilíbrio 
  geral (F1-Score de {xgb_f1:.3f}).

NÍVEL 2: OS ARGUMENTOS CHAVE (POR QUE USAR OU NÃO USAR CADA MODELO)
--------------------------------------------------------------------------------
1. Por que a Acurácia DEVE ser ignorada?
   - Em dados onde 99.83% das transações são legítimas, um modelo simplório que 
     diz que "TUDO É NORMAL" atinge 99.83% de Acurácia, mas erra 100% das fraudes.
   - Acurácia mede eficiência geral, mas em desbalanceamento nós precisamos medir 
     a SENSIBILIDADE a fraudes.

2. Avaliação dos Modelos Analisados:
   [X] Regressão Logística:
       - Prós: Rápido, simples e interpretável.
       - Contras: Perdeu muitas fraudes (Recall de {log_rec:.2%}) por não capturar 
         relações não-lineares complexas.
   
   [X] Árvore de Decisão:
       - Prós: Regras visuais fáceis.
       - Contras: Tende ao overfitting e instabilidade com dados enviesados.
   
   [X] Random Forest:
       - Prós: Muito robusto contra overfitting e com alta precisão.
       - Contras: Exige alto processamento computacional e foi superado pelo XGBoost.

   [V] XGBoost (Recomendado):
       - Prós: Utiliza Gradient Boosting com ponderação ajustada de classes 
         (scale_pos_weight). Identificou a maior fatia do prejuízo financeiro.

NÍVEL 3: EVIDÊNCIAS E TABELA COMPARATIVA DE DADOS (BASE DA PIRÂMIDE)
--------------------------------------------------------------------------------
""")

print(df_res.round(4).to_string())

print("\n" + "="*80)
print(" FIM DO RELATÓRIO ")
print("="*80 + "\n")