import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_diabetes
import pickle

data = load_diabetes(as_frame=True)
df = pd.concat([data.data, data.target.rename("target")], axis=1)

X = df.drop("target", axis=1)
y = df["target"]

model = Pipeline([
    ("scaler", StandardScaler()),
    ("elasticnet", ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42))
])

model.fit(X, y)
pickle.dump(model, open("model.pkl", "wb"))
