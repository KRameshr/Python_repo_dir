import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Machine Learning Imports
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder


# 1. CONFIGURATION & DATA LOADING

COLUMNS = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
    'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
    'hours-per-week', 'native-country', 'income'
]

DATA_PATH = os.path.join('Data-sets', 'adult.csv')

# Load dataset; header=0 skips the CSV text header to prevent string errors
df = pd.read_csv(DATA_PATH, names=COLUMNS, skipinitialspace=True, header=0)


# 2. EXPLORATORY DATA ANALYSIS (EDA)

print("--- Generating Visual Insights ---")

def save_plot(filename):
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Successfully saved: {filename}")

# Visualization: Education vs Income
plt.figure(figsize=(12, 6))
sns.countplot(x='education', hue='income', data=df, palette='viridis')
plt.xticks(rotation=45)
plt.title('Income Distribution by Education Level')
save_plot('income_by_education.png')
plt.show()


# 3. DATA PREPROCESSING

print("\n--- Preprocessing Data ---")

# A. Clean missing values (represented as '?' in this dataset)
df = df.replace('?', pd.NA).dropna()

# B. Encode Categorical Data
# We convert all 'object' types to numerical labels for the ML models
le = LabelEncoder()
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    df[col] = le.fit_transform(df[col].astype(str))

# C. Final conversion to ensure all data is numeric
df = df.apply(pd.to_numeric, errors='coerce').dropna()

# D. Feature & Target Selection
X = df.drop('income', axis=1)
y = df['income']


# 4. MODEL TRAINING & EVALUATION

# Split data into 80% Training and 20% Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Algorithm 1: Logistic Regression (The Baseline)
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

# Algorithm 2: Random Forest (The Powerful Ensemble)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

# Print Results
print("\n" + "="*40)
print(f"LOGISTIC REGRESSION ACCURACY: {accuracy_score(y_test, y_pred_log):.4f}")
print(f"RANDOM FOREST ACCURACY:      {accuracy_score(y_test, y_pred_rf):.4f}")
print("="*40)

print("\nDetailed Classification Report (Random Forest):")
print(classification_report(y_test, y_pred_rf))


# 5. POST-TRAINING VISUALS (INSIGHTS)


# Insight 1: Feature Importance
importances = pd.Series(rf_model.feature_importances_, index=X.columns)
plt.figure(figsize=(10, 6))
importances.nlargest(10).plot(kind='barh', color='darkgreen')
plt.title('Top 10 Drivers of Income Prediction')
save_plot('feature_importance.png')
plt.show()

# Insight 2: Confusion Matrix
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred_rf)
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.title('Confusion Matrix: Random Forest Results')
plt.xlabel('Predicted')
plt.ylabel('Actual')
save_plot('model_confusion_matrix.png')
plt.show()

print("\nProject Complete. All artifacts saved.")