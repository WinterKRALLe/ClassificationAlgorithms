from data_preprocessing import load_and_prepare_data
from model_evaluation import evaluate_classifiers
from visualization import plot_confusion_matrices


def main(city="Albury"):
    """Hlavní funkce pro načtení dat, hodnocení klasifikátorů a predikci deště."""
    df = load_and_prepare_data()

    X = df.drop('RainTomorrow', axis=1).values
    y = df['RainTomorrow'].values

    gnb_matrix, knn_matrix = evaluate_classifiers(X, y)

    plot_confusion_matrices(gnb_matrix, knn_matrix)

    gnb_accuracy = (gnb_matrix[0, 0] + gnb_matrix[1, 1]) / gnb_matrix.sum()
    knn_accuracy = (knn_matrix[0, 0] + knn_matrix[1, 1]) / knn_matrix.sum()

    print(f"Celková přesnost:")
    print(f"Gaussian Naive Bayes: {gnb_accuracy:.3f}")
    print(f"k-Nearest Neighbors: {knn_accuracy:.3f}")


if __name__ == "__main__":
    main()
