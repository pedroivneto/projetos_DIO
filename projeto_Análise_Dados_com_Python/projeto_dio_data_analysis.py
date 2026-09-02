#------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.metrics import classification_report, average_precision_score, precision_recall_curve

# 1. CARREGAMENTO E FEATURE ENGINEERING DA COLUNA 'AMOUNT'
url = 'https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv'

df = pd.read_csv(url) # Seu dataset de 284.807 linhas

# Como 'Amount' tem alta assimetria e outliers, usamos log + RobustScaler
df['Amount_log'] = np.log1p(df['Amount'])
robust_scaler = RobustScaler()
df['Amount_scaled'] = robust_scaler.fit_transform(df[['Amount_log']])

# Separação de atributos e alvo
X = df.drop(columns=['Class', 'Time', 'Amount', 'Amount_log'])
y = df['Class']

# 2. SEPARAÇÃO TREINO/TESTE ESTRATIFICADA
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# 3. CÁLCULO DO PESO DAS CLASSES PARA O XGBOOST
ratio = (y_train == 0).sum() / (y_train == 1).sum() # Apox. 577 para este dataset

# 4. MODELAGEM DO XGBOOST
model_xgb = xgb.XGBClassifier(
    scale_pos_weight=ratio,      # Compensa o desbalanceamento nativamente
    n_estimators=200,
    max_depth=6,
    learning_rate=0.05,
    eval_metric='aucpr',          # Otimiza a curva Precision-Recall durante o treino
    random_state=42,
    n_jobs=-1
)

model_xgb.fit(X_train, y_train)

# 5. AVALIAÇÃO DE PERFORMANCE (Probabilidades)
y_proba_xgb = model_xgb.predict_proba(X_test)[:, 1]

# Métrica principal para comparação no relatório
pr_auc = average_precision_score(y_test, y_proba_xgb)
print(f"XGBoost PR-AUC (AUPRC): {pr_auc:.4f}")

# Avaliação padrão considerando o limiar (threshold) de 0.5
y_pred_xgb = (y_proba_xgb > 0.5).astype(int)
print("\nRelatório de Classificação XGBoost:")
print(classification_report(y_test, y_pred_xgb, target_names=['Legítima', 'Fraude']))