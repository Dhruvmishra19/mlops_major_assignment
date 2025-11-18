cat > train.py <<'EOF'
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

def main():
    data = fetch_olivetti_faces()
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    joblib.dump(clf, "savedmodel.pth")
    print("Model trained and saved as savedmodel.pth")

if __name__ == "__main__":
    main()
EOF
