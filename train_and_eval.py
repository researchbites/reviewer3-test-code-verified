"""Reproducibility harness for the Random Forest baseline on UCI Breast Cancer Wisconsin.

Prints the held-out test accuracy for the fixed hyperparameters described in the paper.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def main() -> None:
    X, y = load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X_train, y_train)
    acc = accuracy_score(y_test, clf.predict(X_test))
    print(f"Test accuracy: {acc * 100:.2f}%")
    print(f"Test samples:  {len(y_test)}")


if __name__ == "__main__":
    main()
