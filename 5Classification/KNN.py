import math
from operator import itemgetter
from collections import Counter
from sklearn import cross_validation
from sklearn.metrics import classification_report
from sklearn.datasets import load_iris

class KNN(object):
    def __init__(self, trainData = None, testData = None, k = 0):
        self.k = k
        self.trainData = trainData
        self.testData = testData

    # Euclidean distance between 2 point
    def dist(self, data1, data2):
        points = zip(data1, data2)
        diffs_squared_distance = [pow(a - b, 2) for (a, b) in points]
        return math.sqrt(sum(diffs_squared_distance))

    # Get k nearest neighbours
    def get_neighbours(self, training_set, test_instance, k):
        distances = [self._get_tuple_distance(training_instance, test_instance) for training_instance in training_set]
        # index 1 is the calculated distance between training_instance and test_instance
        sorted_distances = sorted(distances, key=itemgetter(1))
        # extract only training instances
        sorted_training_instances = [tuple[0] for tuple in sorted_distances]
        # select first k elements
        return sorted_training_instances[:k]

    def _get_tuple_distance(self, training_instance, test_instance):
        return (training_instance, self.dist(test_instance, training_instance[0]))

    # Get most common label
    def get_majority_vote(self, neighbours):
        # index 1 is the class
        classes = [neighbour[1] for neighbour in neighbours]
        count = Counter(classes)
        return count.most_common()[0][0]

    def predict(self):
        predictions = []
        for x in xrange(len(self.testData)):
            neighbours = self.get_neighbours(training_set=self.trainData,
                                             test_instance=self.testData[x][0], k=5)
            majority_vote = self.get_majority_vote(neighbours)
            predictions.append(majority_vote)
        return predictions

def main():
    iris = load_iris()
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.4)
    trainData = zip(X_train, y_train)
    testData = zip(X_test, y_test)
    knn = KNN(trainData, testData, 5)
    y_pred = knn.predict()
    print classification_report(y_test, y_pred)

if __name__ == "__main__":
    main()