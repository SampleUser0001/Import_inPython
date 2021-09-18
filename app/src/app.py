# -*- coding: utf-8 -*-
import sys
import os

from util.SampleUtil import SampleUtil
from research.factory import SuperFactory

if __name__ == '__main__':

  print(sys.path)
  
  SampleUtil.hello_world()
  SampleUtil.hello_by_tmp()

  SuperFactory.create('Sub01').print_message()
  SuperFactory.create('Sub02').print_message()
  
