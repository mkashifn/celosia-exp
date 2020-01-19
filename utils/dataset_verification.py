# Verify if the dataset is present

import os

class Dataset:
  def __init__(self):
    self.name = 'undefined'

  def get_file_list(self):
    return NotImplementedError("method get_file_list must be implemented")

  def get_dir_name(self):
    return NotImplementedError("method get_dir_name must be implemented")

class NbaIoT_Dataset(Dataset):
  def __init__(self):
    self.name = 'N-BaIoT'

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
      file_list.append(f'{i}.benign.csv')
      for g in gafgyt:
        file_list.append(f'{i}.gafgyt.{g}.csv')

      # Filter devices that don't contain mirai attack data
      if d != 'Ennio_Doorbell' and d != 'Samsung_SNH_1011_N_Webcam':
        for m in mirai:
          file_list.append(f'{i}.mirai.{m}.csv')
    
    return file_list

  def get_dir_name(self):
    return 'nbaiot-dataset'


def verify_dataset(name):
  if name == 'nbaiot':
    dataset = NbaIoT_Dataset()
  else:
    raise Exception(f'{name} is not valid, please specify a valid dataset name')
  input_dir = os.path.join('datasets', dataset.get_dir_name())
  file_list = dataset.get_file_list()
  i = 0
  for f in file_list:
    file = os.path.join(input_dir, f)
    if os.path.exists(file):
        #print(f'{i:2}', file)
        i += 1
    else:
        raise Exception(f'{f} is not present in the dataset')
  print (f"Success! {i} data files present in the {dataset.name} dataset.")