# Fetch Data from CSV files
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fetch_data_from_source_list(source_list, anomaly_label=0):
  '''Fetch labeled data from a source list and scale the inputs in 0-1 range.
     Parameters: source_list = a list of data source dictionary with the following
                               attributes:
                      filename = the name of the file including path
                      normal = label 1 for normal and 'anomaly_label' for anomalous entries
                      rows = the number of rows to read, -1 (default) means all rows in the file.
                 anomaly_label = the value to label anomalies, default = 0'''
  l_x = [] # list of features
  l_y = [] # list of labels
  for source in source_list:
    filename = source['filename']
    normal = bool(source['normal'])
    rows = int(source.get('rows', -1))
    print("fetching {} rows from {}".format(rows, filename))
    ds = pd.read_csv(filename, index_col=0)
    if rows >= 0:
      x = ds.iloc[:rows, :].values
    else: # fetch all rows
      x = ds.iloc[:, :].values

    y = np.ones(x.shape[0]) # 1 represents normal
    if not normal: # not normal, label as anomalous
      y = anomaly_label * y

    l_x.append(x)
    l_y.append(y)
  X = np.concatenate(tuple(l_x), axis=0)
  y = np.concatenate(tuple(l_y), axis=0)
  X = np.array(X)
  y = np.array(y)
  y = np.reshape(y, (-1, 1))
  # scale the input in 0-1 range
  sc = MinMaxScaler(feature_range = (0, 1))
  X = sc.fit_transform(X)
  #print ('Shapes = ', X.shape, Y.shape)
  return (X, y)