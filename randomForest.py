from classifier import classifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class RandomForest(classifier):
    def __init__(self, microDataLoc, estimators=55, depth=7):
        classifier.__init__(self, microDataLoc)
        self.estimators = estimators
        self.depth = depth

    def train(self):
        train, test, trainLabel, testLabel = self.trainTestSplit()
        clf = [RandomForestClassifier(n_estimators=self.estimators, max_depth=self.depth, random_state=41) for i in range(self.clusterNum)]
        for i in range(self.clusterNum):
            clf[i].fit(train[i], trainLabel[i])
        return (clf, test, testLabel) # return test and testLabel to self.test() so no need to
                                      # recompute the testing data again

if __name__ == "__main__":
    
    depth = map(int, np.linspace(2, 10, 4))
    estimators = map(int, np.linspace(5, 200, 20))

    for i in depth:
        for j in estimators:
            print 'for depth = %s and estimators = %s'%(i, j)
            apple = RandomForest("data/appleTrainData.txt", j, i)
            apple.reportResult()
            print '\n'

