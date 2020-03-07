import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm


class Kmeans:

    def __init__(self, n_clusters, max_iter=30, random_state=123):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
        self.old_centroids=None

    def initializ_centroids(self, X):
        np.random.RandomState(self.random_state)
        random_idx = np.random.permutation(X.shape[0])
        centroids = X[random_idx[:self.n_clusters]]
        return centroids

    def compute_centroids(self, X, labels):
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            centroids[k, :] = np.mean(X[labels == k, :], axis=0)
        return centroids

    def compute_distance(self, X, centroids):
        distance = np.zeros((X.shape[0], self.n_clusters))
        for k in range(self.n_clusters):
            row_norm = norm(X - centroids[k, :], axis=1)
            distance[:, k] = np.square(row_norm)
        return distance

    def find_closest_cluster(self, distance):
        return np.argmin(distance, axis=1)

    def compute_sse(self, X, labels, centroids):
        distance = np.zeros(X.shape[0])
        for k in range(self.n_clusters):
            distance[labels == k] = norm(X[labels == k] - centroids[k], axis=1)
        return np.sum(np.square(distance))
    
    def fit(self, X):
        self.centroids = self.initializ_centroids(X)
        for i in range(self.max_iter):
            self.old_centroids = self.centroids
            distance = self.compute_distance(X, self.old_centroids)
            self.labels = self.find_closest_cluster(distance)
            self.centroids = self.compute_centroids(X, self.labels)
            if np.all(self.old_centroids == self.centroids):
                break
        self.error = self.compute_sse(X, self.labels, self.centroids)
    
    def predict(self, X):
        distance = self.compute_distance(X, self.old_centroids)
        return self.find_closest_cluster(distance)
if __name__=="__main__":
    model=Kmeans(3)
    img=plt.imread("Buttryfly.jpg")
    if len(img.shape)==2:
        res=img.reshape(-1,2)
    else:
        res=img.reshape(-1,3)
    print(res.shape)
    model.fit(res)
    out=model.predict(res)
    plt.imshow(out.reshape(img.shape[:2]))
    plt.show()