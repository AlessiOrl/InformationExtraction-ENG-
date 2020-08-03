from abc import abstractmethod
import os


class Extraction:

    def __init__(self, filename):
        self.filename = filename
        self.__NameDict = {}

        def extractname():
            path = "../data/tagged/" + os.path.splitext(self.filename)[0] + ".tagged"
            with open(path) as FileObj:
                for line in FileObj:
                    i = line[:-1].split("\t")
                    if i[2] != "PER": continue
                    if i[3] in self.__NameDict.keys():
                        self.__NameDict[i[3]] += 1
                    else:
                        self.__NameDict[i[3]] = 1
            return
        extractname()


    @abstractmethod
    def extract(self):
        pass

    def get__NameDict(self):
        return self.__NameDict

    def getpath(self):
        return self.path
