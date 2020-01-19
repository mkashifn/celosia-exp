# Dataset abstract class

class Dataset(object):
  def __init__(self):
    self.name = 'undefined'
    self.dir_base = 'datasets'

  def get_name(self):
    return NotImplementedError("method get_name must be implemented")

  def get_file_list(self):
    return NotImplementedError("method get_file_list must be implemented")

  def get_dir_name(self):
    return NotImplementedError("method get_dir_name must be implemented")