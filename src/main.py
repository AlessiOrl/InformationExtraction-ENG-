from src.relex import *


def main():
  s1 = SimpleExtraction("data/tagged/11_alices_adventures_in_wonderland.tagged")
  print("-----------------------------")
  s1.extract()


main()
