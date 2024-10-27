import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler


def evaluate_classifiers(X, y, n_splits=10):
    """Hodnotí Gaussian Naive Bayes a k-Nearest Neighbors klasifikátory pomocí cross-validation."""
    gnb = GaussianNB()
    knn = KNeighborsClassifier(n_neighbors=5)
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    scaler = StandardScaler()

    gnb_conf_matrix = np.zeros((2, 2))
    knn_conf_matrix = np.zeros((2, 2))

    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # Standardizace trénovacích a testovacích dat v každém fold
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        gnb.fit(X_train_scaled, y_train)
        gnb_pred = gnb.predict(X_test_scaled)
        gnb_conf_matrix += confusion_matrix(y_test, gnb_pred)

        knn.fit(X_train_scaled, y_train)
        knn_pred = knn.predict(X_test_scaled)
        knn_conf_matrix += confusion_matrix(y_test, knn_pred)

    return gnb_conf_matrix, knn_conf_matrix
