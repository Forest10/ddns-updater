#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# 解决'ascii' codec can't decode byte 0xe5 in position 26: ordinal not in range(128)
import sys

reload(sys)
sys.setdefaultencoding('utf8')
# 解决'ascii' codec can't decode byte 0xe5 in position 26: ordinal not in range(128)
