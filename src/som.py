from thirdparty.minisom import MiniSom
from pylab import bone, pcolor, colorbar, plot, show

class Som:
  def __init__(self, x=20, y=None):
    '''
      parameter: x, y, size of the grid,
                 default: 20x20, if y is not supplied, y is the same as x
    '''
    self.som = None
    self.map_x = x
    if not y:
      self.map_y = x # square grid
    else:
      self.map_y = y

  def fit(self, X):
    '''
      Fit SOM to the input data.
        Parameters: X = a numpy array and it should contain
                        all columns as features and any manually
                        labeled columns should be removed before
                        calling this function.
    '''
    nb_features = X.shape[1] # number of features
    som = MiniSom(x = self.map_x, y = self.map_y, input_len = nb_features, sigma = 1.0, learning_rate = 0.5)
    som.random_weights_init(X)
    som.train_random(data = X, num_iteration = 2000)
    dm = som.distance_map()
    mid = []
    for x in X:
      w = som.winner(x)
      (x,y) = w
      mid.append(dm[x][y])

    self.dm = dm
    self.som = som
    self.grid = (self.map_x, self.map_y)
    self.mid = mid

  def predict(self, threshold = 0.02, anomaly_label=0):
    '''Predict data as normal or anomalous based upon mean inter-neuron distance.
       Need to call fit() before calling this.
       Parameters: threshold = the threshold (default = 0.02) that is used to
                               determine if normal = 1 (when mid <= threshold),
                               or anomalous = 0 otherwise.
                   anomaly_label = the value to label anomalies, default = 0'''
    if self.som is None:
      raise Exception('Call fit() before calling this')

    y_pred = []
    for m in self.mid:
      normal = (1 if m <= threshold else anomaly_label)
      y_pred.append(normal)
    return y_pred

  def plot_marker(self, xy, m, c):
    plot(xy[0] + 0.5,
         xy[1] + 0.5,
         m,
         markeredgecolor = c,
         markerfacecolor = 'None',
         markersize = 10,
         markeredgewidth = 2)

  def plot_distance_map_labels(self, X, Y):
    '''Plots distance map with labels. Need to call fit() before calling this.
       Parameters: X = input features
                   Y = labels, 1 = normal, 0 = anomalous.'''
    if self.som is None:
      raise Exception('Call fit() before calling this')

    red_set = set() # normal instances
    green_set = set() # anomalous instances
    for i, x in enumerate(X):
        w = self.som.winner(x)
        if int(Y[i]) == 0:
            red_set.add(w)
        else:
            green_set.add(w)
    bone()
    pcolor(self.dm.T)
    colorbar()
    (map_x, map_y) = self.grid
    for x in range(map_x):
      for y in range(map_y):
         xy = (x,y)
         if (xy in red_set) and (xy in green_set):
             self.plot_marker(xy, 'h', 'y')
         elif xy in red_set:
             self.plot_marker(xy, 'o', 'r')
         elif xy in green_set:
             self.plot_marker(xy, 's', 'g')
         else:
             pass #plot_marker(xy, 'v', 'b')
    show()