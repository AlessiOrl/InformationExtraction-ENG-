from . import Extraction


class SimpleExtraction(Extraction):



  def extract(self):
    with open(self.path) as FileObj:
      for lines in FileObj:
        print(lines)  # or do some other thing with the line...