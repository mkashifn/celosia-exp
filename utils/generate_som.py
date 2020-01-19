# Generate SOM for a device

from src.nbaiot import NbaIoT_Dataset
from src.som import Som
from utils.fetch_data import fetch_data_from_source_list

def select_data(source_list):
  selected_source_list = []
  for source in source_list:
    if source['normal']:
      source['rows'] = 4000
    else:
      source['rows'] = 50

    selected_source_list.append(source)
  return selected_source_list

def fetch_device_data(name):
  nbaiot = NbaIoT_Dataset()
  source_list = nbaiot.get_source_list_by_name(name)
  source_list = select_data(source_list)

  (X, y) = fetch_data_from_source_list(source_list)
  print (X, y)
  print (X.shape, y.shape)
  som = Som()
  som.fit(X)
  som.plot_distance_map_labels(X, y)
  y_pred = som.predict()
  print(y_pred)
