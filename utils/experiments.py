# Run experiments

from src.nbaiot import NbaIoT_Dataset
from src.som import Som
from utils.fetch_data import fetch_data_from_source_list
from utils.persistence import store_object, load_object
from sklearn.metrics import accuracy_score, precision_recall_curve, classification_report, confusion_matrix, average_precision_score, roc_curve, auc
from utils.metrics import get_accuracy

class Experiment:
  def __init__(self):
    pass

  def select_data(self, source_list):
    selected_source_list = []
    for source in source_list:
      if source['normal']:
        source['rows'] = 4000
      else:
        source['rows'] = 50

      selected_source_list.append(source)
    return selected_source_list

  def show_report(self, title, y_true, y_pred):
    print ("========================")
    print(title)
    
    print ("")
    print ("Classification Report: ")
    print (classification_report(y_true, y_pred))
    print ("")
    print ("Accuracy Score: ", accuracy_score(y_true, y_pred))
    
    print ("Confusion Matrix: ")
    print (confusion_matrix(y_true, y_pred))

    print ("Accuracy Metrics: ")
    print (get_accuracy(y_true, y_pred))
    print ("========================")

  def compute_som_accuracy_vs_threshold(self, device_id):
    dataset = NbaIoT_Dataset()
    index = device_id - 1
    name = dataset.get_device_name_by_index(index)

    print("Starting to compute SOM accuracy vs threshold for {}".format(name))
    source_list = dataset.get_source_list_by_index(index)
    source_list = self.select_data(source_list)

    (X, y) = fetch_data_from_source_list(source_list)
    #print(X, y)
    print(X.shape, y.shape)
    som = Som()
    som.fit(X)

    #som_filename = "{}-som.kn".format(name)
    #data_filename = "{}-Xy.kn".format(name)

    #store_object(som, som_filename)
    #store_object((X, y), data_filename)

    #som_loaded = load_object(som_filename)
    #(X_loaded, y_loaded) = load_object(data_filename)
    (X_loaded, y_loaded) = (X, y)
    som_loaded = som

    step = 0.01
    threshold = 0
    i = 1
    while threshold <= 1:
      y_pred = som.predict(threshold)
      self.show_report('{} - Threshold={}'.format(i, threshold), y_loaded, y_pred)
      threshold += step
      i += 1

    #som_loaded.plot_distance_map_labels(X_loaded, y_loaded)
