from abc import abstractmethod


class Extraction:
  __NameList = None

  @staticmethod
  def getNameList():
    """ Static access method. """
    if Extraction.__NameList is None: __NameList = []
    return Extraction.__NameList

  def __init__(self, path):
    self.path = path

  def extractName(self):



  @abstractmethod
  def extract(self): pass

