cat > test.py <<'EOF'
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def main():
    data = fetch_olivetti_faces()
    X, y = data.data, data.target

    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    clf = joblib.load("savedmodel.pth")
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"Test Accuracy: {acc:.4f}")

if __name__ == "__main__":
    main()
EOF
