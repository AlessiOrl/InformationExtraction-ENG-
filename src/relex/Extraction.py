from abc import abstractmethod


class Extraction:
  def __init__(self, path):
    self.path = path


  @abstractmethod
  def extract(self): pass

