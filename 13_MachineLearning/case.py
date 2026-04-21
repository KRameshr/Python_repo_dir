
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression # Using Linear for r2_score
from sklearn.metrics import r2_score

# 1. Import the wine dataset
wine = load_wine()
# Convert to DataFrame for easier handling
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
df['target'] = wine.target

# 2. Split the data into train and test set (80/20 split)
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Make Predictions
predictions = model.predict(X_test)

# 5. Check performance using r2_score
score = r2_score(y_test, predictions)
print(f"Model R2 Score: {score:.4f}")