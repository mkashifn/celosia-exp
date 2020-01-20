# N-BaIoT dataset
import os
from src.dataset import Dataset

class NbaIoT_Dataset(Dataset):
  def __init__(self):
    super(NbaIoT_Dataset, self).__init__()
    self.name = 'N-BaIoT'
    self.dir_dataset = 'nbaiot-dataset'
    self.devices = ['Danmini_Doorbell', 'Ecobee_Thermostat', 'Ennio_Doorbell', 'Philips_B120N10_Baby_Monitor', 'Provision_PT_737E_Security_Camera', 'Provision_PT_838_Security_Camera', 'Samsung_SNH_1011_N_Webcam', 'SimpleHome_XCS7_1002_WHT_Security_Camera', 'SimpleHome_XCS7_1003_WHT_Security_Camera']

    self.gafgyt = ['combo', 'junk', 'scan', 'tcp', 'udp']
    self.mirai = ['ack', 'scan', 'syn', 'udp', 'udpplain']

  def get_name(self):
    return self.name

  def add_to_source_list(self, source_list, filename, normal):
    filename = os.path.join(self.dir_base, self.dir_dataset, filename)
    source = {'filename': filename, 'normal': normal}
    source_list.append(source)

  def get_device_index_by_name(self, name):
    return self.devices.index(name)

  def get_device_name_by_index(self, index):
    return self.devices[index]

  def get_source_list_by_name(self, name):
    index = self.devices.index(name)
    return self.get_source_list_by_index(index)

  def get_source_list_by_index(self, index):
    # Returns source list for 9 commercial devices as follows:
    #   Each device contains 1x benign data file and 5x gafgyt attacks (9 x 6 = 54 files).
    #   7 devices contain 5x mirai attacks data each (7 x 5 = 35 data files)
    # Total: (54 + 35) 89 data files.

    if index < 0 or index >= len(self.devices):
      raise Exception('index value of {} is out of range'.format(index))

    source_list = []

    i = index + 1
    d = self.devices[index]

    # Benign traffic, (normal)
    filename = '{}.benign.csv'.format(i)
    self.add_to_source_list(source_list, filename, True)

    # Gafgyt traffic, (anomalous)
    for g in self.gafgyt:
      filename = '{}.gafgyt.{}.csv'.format(i, g)
      self.add_to_source_list(source_list, filename, False)

    # Mirai traffic, (anomalous)
    # Filter devices that don't contain mirai attack data
    if d != 'Ennio_Doorbell' and d != 'Samsung_SNH_1011_N_Webcam':
      for m in self.mirai:
        filename = '{}.mirai.{}.csv'.format(i, m)
        self.add_to_source_list(source_list, filename, False)

    return source_list
  
  def get_file_list(self):
    
    source_list = []
    file_list = []

    for i in range(len(self.devices)):
      source_list.extend(self.get_source_list_by_index(i))

    for s in source_list:
      file_list.append(s['filename'])

    return file_list

  def get_dir_name(self):
    return self.dir_dataset

