#!/usr/bin/env python3
# k_means_spectral.py


from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, SpectralClustering
import matplotlib.pyplot as plt
import sys
import os


def plot_kmeans(ax, X, y):
    ax.set_title(f"k-Means Clustering")
    labels = KMeans(2, random_state=0).fit_predict(X)
    ax.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap="viridis")


def plot_spectral(ax, X, y):
    ax.set_title(f"Spectral Clustering")
    model = SpectralClustering(
        n_clusters=2, affinity="nearest_neighbors", assign_labels="kmeans"
    )  # want two clusters, pass in x and y data
    labels = model.fit_predict(X)  # predict cluster containing a data point
    ax.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap="viridis")


def main():
    X, y = make_moons(200, noise=0.05, random_state=0)  # make 200 moons

    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(2, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot_kmeans(ax, X, y)

    ax = fig.add_subplot(gs[1, 0])
    plot_spectral(ax, X, y)

    print(X)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
