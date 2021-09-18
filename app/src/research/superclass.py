# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class SuperClass(metaclass=ABCMeta):
  @abstractmethod
  def print_message():
    pass

