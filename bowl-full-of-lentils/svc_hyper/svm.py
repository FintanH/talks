import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split

def train_and_predict(X_train, y_train, X_test, y_test, gammas, cs):
    for gamma in gammas:
        for c in cs:
            svc = svm.SVC(kernel="rbf", gamma=gamma, C=c).fit(X_train, y_train)

            print("GAMMA=%f, C=%f" % (gamma, c))
            predictions = svc.predict(X_test) == y_test
            print("PREDICTION=%f\n\n" % (sum(predictions) / len(predictions)))

def main():
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    gammas = [0.1, 1, 10, 100]
    cs = [0.1, 1, 10, 100, 1000]

    train_and_predict(X_train, y_train, X_test, y_test, gammas, cs)
