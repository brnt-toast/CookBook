#!/usr/bin/env python3

import os

def mkdir(target):
  return os.mkdir(f'{os.curdir}/{target}')
