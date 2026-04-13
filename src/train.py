import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load data
data = pd.read_csv('../data/student_data.csv')

# Features & target
X = data[['hours_study','hours_sleep', 'attendance', 'previous_marks']]
y = data['pass']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('../model/model.pkl', 'wb'))

print("✅ Model trained and saved successfully!")

# After prediction
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc * 100:.2f}%")