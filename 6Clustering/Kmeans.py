import numpy as np
import random
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

class KMeans(object):
    def __init__(self, trainData = None, k = 0):
        self.k = k
        self.trainData = trainData

    def cluster_points(self, centroids):
        clusters = {}
        for x in self.trainData:
            bestmukey = min([(i[0], np.linalg.norm(x - centroids[i[0]])) \
                             for i in enumerate(centroids)], key=lambda t: t[1])[0]
            try:
                clusters[bestmukey].append(x)
            except KeyError:
                clusters[bestmukey] = [x]
        return clusters

    def reevaluate_centers(self, clusters):
        newmu = []
        keys = sorted(clusters.keys())
        for k in keys:
            newmu.append(np.mean(clusters[k], axis=0))
        return newmu

    def has_converged(self, centroids, old_centroids):
        return (set([tuple(a) for a in centroids]) == set([tuple(a) for a in old_centroids]))

    def fit_predict(self):
        # Initialize to K random centers
        old_centroids = random.sample(self.trainData, self.k)
        centroids = random.sample(self.trainData, self.k)
        while not self.has_converged(centroids, old_centroids):
            old_centroids = centroids
            # Assign all points in X to clusters
            clusters = self.cluster_points(centroids)
            # Reevaluate centers
            centroids = self.reevaluate_centers(clusters)
        return (centroids, clusters)

def main():
    iris = load_iris()
    X = iris.data[:, :2]
    km = KMeans(X, 3)
    clusters = km.fit_predict()
if __name__ == "__main__":
    main()