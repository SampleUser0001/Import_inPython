# -*- coding: utf-8 -*-
import sys
sys.path.append('./')
from util.tmp.sample import SampleUtil02

class SampleUtil:

  @classmethod
  def hello_world(cls):
    print("Hello World!")

  @staticmethod
  def hello_by_tmp():
    SampleUtil02.hello_world()