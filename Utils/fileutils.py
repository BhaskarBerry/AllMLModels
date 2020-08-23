# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:37:37 2019

@author: BBerry
"""

def readFile(filename):
    filehandle = open(filename)
    print(filehandle.read())
    filehandle.close()