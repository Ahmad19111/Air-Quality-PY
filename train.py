import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv("data/city_day.csv")

# Drop rows with missing target values (AQI and AQI_Bucket)
df = df.dropna(subset=["AQI", "AQI_Bucket"])

# Select specific features for the model
df = df[["PM2.5", "NO2", "CO", "SO2", "O3", "AQI_Bucket"]]

# Impute missing values in features using the median
gases = ["PM2.5", "NO2", "CO", "SO2", "O3"]
for gas in gases:
    df[gas]=df[gas].fillna(df[gas].median())


# Split data into features (X) and target (y)
X = df.drop(columns=["AQI_Bucket"])
y = df["AQI_Bucket"]

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators= 100, random_state = 42)
model.fit(X_train,y_train)

# Evaluate the model
prediction = model.predict(X_test)
score = accuracy_score(y_test, prediction)
print(f"Model Accuracy (V1.0): {score * 100:.2f}%")

# Save the trained model to the models directory
joblib.dump(model, "models/air_quality_model_v1.pkl")
print("Model savedscssessfuly in model/ directory")