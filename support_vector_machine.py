import matplotlib.pylot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

# matplotlib for plotting & numpy for handling arrays as we have a lot of that.

class Support_Vector_Machine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors = {1:'r', -1:'b'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)

    # trains our SVM.  Optimization step.
    def fit(self, data):
        self.data = data
        # we'll create a dictionary with key as magnitude of vector w &
        # respective elements as vector w & b
        # Remember here we are looking for w with minimum magnitude & b with largest magnitude that
        # satisfy this eqn. yi(xi.w + b ) = 1
        # { ||w||: [w,b] }
        opt_dict = {}

        # we make transforms to assure that all versions of the vector are checked

        transforms = [[1,1],
                      [-1,1],
                      [-1,-1],
                      [1,-1]]

        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None

        step_sizes = [self.max_feature_value * 0.1,
                      self.max_feature_value * 0.01,
                      # point of expense:
                      self.max_feature_value * 0.001,]

        # extremely expensive
        b_range_multiple = 5
        #
        b_multiple = 5
        latest_optimum = self.max_feature_value*10

        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
            # we can do this because of convex nature
            optimized = False
            while not optimized:
                pass



    # Predicts the value of a new featureset, after training the classifier
    # sign(x.w + b) is the result.
    def predict(self, features):
        # sign( x.w + b)
        classification = np.sign(np.dot(np.array(features),self.w)+self.b)

        return classification

data_dict = {-1:np.array([[1,7],
                          [2,8],
                          [3,8],]),
             1:np.array([[5,1],
                         [6,-1],
                         [7,3],])}

