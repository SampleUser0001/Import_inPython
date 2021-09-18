# -*- coding: utf-8 -*-
from research.sub01 import Sub01
from research.sub02 import Sub02

class SuperFactory:
  @staticmethod
  def create(classname):
    if classname == 'Sub01':
      return Sub01()
    elif classname == 'Sub02':
      return Sub02()
    else:
      raise ValueError('引数は"Sub01"か"Sub02"を渡してください。')
