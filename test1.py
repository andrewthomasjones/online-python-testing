from pprint import pprint
from river import datasets

dataset = datasets.Phishing()

for x, y in dataset:
    pprint(x)
    print(y)
    break

from river import compose
from river import linear_model
from river import metrics
from river import preprocessing

model = compose.Pipeline(
    preprocessing.StandardScaler(),
    linear_model.LogisticRegression()
    )

metric = metrics.Accuracy()

for x, y in dataset:
    y_pred = model.predict_one(x)      # make a prediction
    metric = metric.update(y, y_pred)  # update the metric
    model = model.learn_one(x, y)      # make the model learn

metric
