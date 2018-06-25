#!/usr/bin/env python2
# coding:utf-8

def write2file(filepath, str):
    file
    f = open(filepath, 'wb')
    f.write(str)
    f.flush()
    f.close()


def readfirstline(filename):
    file
    rf = open(filename)
    return rf.readline()


def strinlineequal(str1, str2):
    return str1.__eq__(str2 + '\n')
