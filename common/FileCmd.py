#!/usr/bin/env python2
# coding:utf-8

import os

import time


def createTimeBaseFolder():
    folder = time.strftime(r"%Y-%m-%d_%H-%M-%S", time.localtime())

    os.makedirs(r'%s/%s' % (os.getcwd(), folder))


if __name__ == '__main__':
    createTimeBaseFolder()
