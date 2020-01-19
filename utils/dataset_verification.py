# Verify if the dataset is present

import os

class Dataset:
  def __init__(self):
    self.name = 'undefined'

  def get_name(self):
    return NotImplementedError("method get_name must be implemented")

  def get_file_list(self):
    return NotImplementedError("method get_file_list must be implemented")

  def get_dir_name(self):
    return NotImplementedError("method get_dir_name must be implemented")

class NbaIoT_Dataset(Dataset):
  def __init__(self):
    self.name = 'N-BaIoT'

  def get_name(self):
    return self.name

  def get_file_list(self):
    # Returns all the 89 data files for 9 commercial devices as follows:
    #   Each device contains 1x benign data file and 5x gafgyt attacks (9 x 6 = 54 files).
    #   7 devices contain 5x mirai attacks data each (7 x 5 = 35 data files)
    # Total: (54 + 35) 89 data files.

    devices = ['Danmini_Doorbell', 'Ecobee_Thermostat', 'Ennio_Doorbell', 'Philips_B120N10_Baby_Monitor', 'Provision_PT_737E_Security_Camera', 'Provision_PT_838_Security_Camera', 'Samsung_SNH_1011_N_Webcam', 'SimpleHome_XCS7_1002_WHT_Security_Camera', 'SimpleHome_XCS7_1003_WHT_Security_Camera']
    gafgyt = ['combo', 'junk', 'scan', 'tcp', 'udp']
    mirai = ['ack', 'scan', 'syn', 'udp', 'udpplain']
    file_list = []
    for i, d in enumerate(devices, 1):
      file_list.append('{}.benign.csv'.format(i))
      for g in gafgyt:
        file_list.append('{}.gafgyt.{}.csv'.format(i, g))

      # Filter devices that don't contain mirai attack data
      if d != 'Ennio_Doorbell' and d != 'Samsung_SNH_1011_N_Webcam':
        for m in mirai:
          file_list.append('{}.mirai.{}.csv'.format(i, m))
    
    return file_list

  def get_dir_name(self):
    return 'nbaiot-dataset'


def verify_dataset(name):
  if name == 'nbaiot':
    dataset = NbaIoT_Dataset()
  else:
    raise Exception('{} is not valid, please specify a valid dataset name'.format(name))
  input_dir = os.path.join('datasets', dataset.get_dir_name())
  file_list = dataset.get_file_list()
  i = 0
  for f in file_list:
    file = os.path.join(input_dir, f)
    if os.path.exists(file):
        #print(f'{i:2}', file)
        i += 1
    else:
        raise Exception('{} is not present in the dataset'.format(f))
  print ("Success! {} data files present in the {} dataset.".format(i, dataset.get_name()))