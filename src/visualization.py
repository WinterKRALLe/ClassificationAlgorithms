import matplotlib.pyplot as plt
import seaborn as sns


def plot_confusion_matrices(gnb_matrix, knn_matrix):
    """Vykreslí matice záměn pro oba klasifikátory."""
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    labels = ['Žádný déšť', 'Déšť']

    sns.heatmap(gnb_matrix, annot=True, fmt='.0f', cmap='Blues', ax=ax1,
                xticklabels=labels, yticklabels=labels)
    ax1.set_title('Gaussian Naive Bayes\nKontingenční tabulka')
    ax1.set_xlabel('Predikovaná třída')
    ax1.set_ylabel('Skutečná třída')

    sns.heatmap(knn_matrix, annot=True, fmt='.0f', cmap='Blues', ax=ax2,
                xticklabels=labels, yticklabels=labels)
    ax2.set_title('k-Nearest Neighbors\nKontingenční tabulka')
    ax2.set_xlabel('Predikovaná třída')
    ax2.set_ylabel('Skutečná třída')

    plt.tight_layout()
    plt.savefig("results/Contingency_table.png")
