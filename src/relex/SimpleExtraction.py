from . import Extraction


class SimpleExtraction(Extraction):

  def extract(self):
    print("i'm extracting " + self.path)
