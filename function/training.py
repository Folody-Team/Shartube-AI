"""
  Copyright (c) 2021, Folody Studio
  >>> input -> x: image, y: image
  >>> output -> training 
"""
import os
import csv
import numpy as np

from PIL import Image
from collections import Counter

# format files
format_files = ['jpg', 'jpeg', 'png', 'bmp', 'gif']

class training:
    def __init__(self, filepath):
      self.filepath = filepath
    """
      create image list from path
      >>> input -> filepath: string
      >>> output -> image_list: list
    """
    def createImageList(self):
      filelist = []
      args = self.filepath.split('/')
      dirname = args[0]
      print(dirname)
      for root, dirs, files in os.walk(dirname, topdown=False):
        for name in files:
          for format in format_files:
            if name.endswith(format):
              filelist.append(os.path.join(root, name))
      return filelist

    def csvConvert(self, ouput):
      print('[INFO] Convert csv file')
      filelist = self.createImageList()

      for file in filelist:
        image = Image.open(file)
        image_g = image.convert('L')

        size = {'1': image_g.size[0], '2': image_g.size[1]}

        value = np.asarray(image_g.getdata(), dtype=np.int).reshape(
          (size['1'], size['2'])
        )
        value = value.flatten()
        valuelist = value.tolist()
        valuestringlist = [str(i) for i in valuelist]
        valuelist = valuestringlist
        symbol = {i for i in valuelist}

        pers = []

        for v in zip(*valuelist):
          count = Counter(v)
          total = sum(count.values())

          per = {key: value/total for key, value in count.items()}

          pers.append([per.get(i, 0.0) for i in sorted(symbol)]) 

        for index, item in enumerate(zip(*valuelist)):
          print(pers[index])

        with open(ouput, 'a') as f:
          csv_writer = csv.writer(f)
          csv_writer.writerow(value)
      
      print('[INFO] Convert csv file complete')
