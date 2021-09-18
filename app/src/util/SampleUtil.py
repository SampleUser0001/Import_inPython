# -*- coding: utf-8 -*-
from util.tmp.common import SampleUtil02

class SampleUtil:

  @classmethod
  def hello_world(cls):
    print("Hello World!")

  @staticmethod
  def hello_by_tmp():
    SampleUtil02.hello_world()
