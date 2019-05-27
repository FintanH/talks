import json
import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
import sys

def train_and_predict(X_train, y_train, X_test, y_test, gamma, C):
    svc = svm.SVC(kernel="rbf", gamma=gamma, C=C).fit(X_train, y_train)

    print("GAMMA=%f, C=%f" % (gamma, C))
    predictions = svc.predict(X_test) == y_test
    print("PREDICTION=%f\n\n" % (sum(predictions) / len(predictions)))

def main():
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    file_name = sys.argv[1]
    print("Loading: %s" % file_name)
    with open(file_name, "r") as fp:
        hyperparameters = json.load(fp=fp)

    for param in hyperparameters:
        train_and_predict(X_train, y_train, X_test, y_test, **param)

main()
