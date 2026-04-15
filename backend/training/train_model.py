from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# training data
X = np.array([[500], [800], [1000], [1500], [2000]])
y = np.array([150000, 200000, 250000, 350000, 450000])

# train model
model = LinearRegression()
model.fit(X, y)

# save model
joblib.dump(model, "house_price_model.pkl")

print("Model trained and saved!")