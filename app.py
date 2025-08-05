from flask import Flask, request, render_template
import pickle
import pandas as pd
from sklearn.datasets import load_diabetes

data = load_diabetes(as_frame=True)
feature_names = list(data.feature_names)

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("home.html", features=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    input_vals = {f: float(request.form[f]) for f in feature_names}
    df = pd.DataFrame([input_vals])
    pred = model.predict(df)[0]
    return render_template("result.html", prediction=round(pred, 2))

if __name__ == "__main__":
    app.run(debug=True)
