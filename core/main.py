from function import training as tr
import sys

def init(pathfile):
  train = tr.training(pathfile)
  train.csvConvert()