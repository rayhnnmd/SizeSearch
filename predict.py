import joblib
import numpy as np

model = joblib.load("clothing_size_model.joblib")

label_map = {0:"S", 1:"M", 2:"L", 3:"XL"}

def predict_size(weight, age, height):
    x = np.array([[weight, age, height]])
    label = model.predict(x)[0]
    return label_map[label]

# For an example
print(predict_size(78, 19, 180))

