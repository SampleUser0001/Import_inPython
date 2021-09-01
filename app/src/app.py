# -*- coding: utf-8 -*-
import sys
sys.path.append('./util')
from SampleUtil import SampleUtil

# これでもOK。
# sys.path.append('./')
# from util.SampleUtil import SampleUtil

if __name__ == '__main__':
  SampleUtil.hello_world()
