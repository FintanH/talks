import json
import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
import sys

def train_and_predict(kernel, X_train, y_train, X_test, y_test, gamma, C):
    svc = svm.SVC(kernel=kernel, gamma=gamma, C=C).fit(X_train, y_train)
    predictions = svc.predict(X_test) == y_test
    return (gamma, C, sum(predictions) / len(predictions))

def main():
    trainer_file = sys.argv[1]
    params_file = sys.argv[2]

    print("Loading trainer: %s" % trainer_file)
    with open(trainer_file, "r") as fp:
        trainer = json.load(fp=fp)

    print("Loading params: %s" % params_file)
    with open(params_file, "r") as fp:
        hyperparameters = json.load(fp=fp)

    if trainer["dataset"] == "Iris":
        dataset = datasets.load_iris()
    else if trainer["dataset"] == "Wine":
        dataset = datasets.load_wine()
    else:
        raise Exception("Unknown dataset param: %s" dataset)

    X = dataset.data[:, :2]
    y = dataset.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    for param in hyperparameters:
        (gamma, C, accuracy) = train_and_predict(trainer["kernel"].lower(), X_train, y_train, X_test, y_test, **param)
        print("GAMMA=%f, C=%f" % (gamma, C))
        print("ACCURACY=%f\n\n" % accuracy)
main()
