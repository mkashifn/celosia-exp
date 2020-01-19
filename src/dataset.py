# Dataset abstract class

class Dataset:
  def __init__(self):
    self.name = 'undefined'

  def get_name(self):
    return NotImplementedError("method get_name must be implemented")

  def get_file_list(self):
    return NotImplementedError("method get_file_list must be implemented")

  def get_dir_name(self):
    return NotImplementedError("method get_dir_name must be implemented")