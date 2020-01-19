# Verify if the dataset is present
import os
from src.nbaiot import NbaIoT_Dataset

def verify_dataset(name):
  if name == 'nbaiot':
    dataset = NbaIoT_Dataset()
  else:
    raise Exception('{} is not valid, please specify a valid dataset name'.format(name))
  file_list = dataset.get_file_list()
  i = 0
  for f in file_list:
    if os.path.exists(f):
        #print(f'{i:2}', file)
        i += 1
    else:
        raise Exception('{} is not present in the dataset'.format(f))
  print ("Success! {} data files present in the {} dataset.".format(i, dataset.get_name()))