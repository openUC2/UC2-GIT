#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 16:54:52 2021

@author: bene
"""

import string
import json as json
import os

import xlrd


class uc2_application:
    def __init__(self, name, description, githublink, image, price):
        self.name = name
        self.description = description
        self.githublink = githublink
        self.image = image
        self.price = price
        self.type = 'application'
        self.is_box = False        

        if self.name.find('BOX')>0:
            self.is_box = True
            
        
        self.modules = []
        

    def addmodule(self, module):
        self.modules.append(module)

    def print(self):
        print("App Name: " + self.name)
        print("App description: " + self.description)
        print("App githublink: " + self.githublink)
        print("App image: " + self.image)
        print("App Parts: ".join(str(x) for x in ([i.name for i in self.modules]))) 

class uc2_module: # also called assembly
    def __init__(self, name, description, githublink, image, price):
        self.name = name
        self.description = description
        self.githublink = githublink
        self.image = image
        self.price = price
        self.fixedOptions = {}
        self.type = "module"
        
        self.partslist = []
        
    def addpart(self, part):
        self.partslist.append(part)

    def print(self):
        print("Module Name: " + self.name)
        print("Module description: " + self.description)
        print("Module githublink: " + self.githublink)
        print("Module image: " + self.image)
        print("Module Parts: ".join(str(x) for x in ([i.name for i in self.partslist]))) 


class uc2_part:
    def __init__(self, name, description, githublink, image, price, is_printable, n_parts):
        self.name = name
        self.description = description
        self.githublink = githublink
        self.image = image
        self.price = price
        self.is_printable = is_printable
        self.n_parts = n_parts
        
    def print(self):
        print("App Name: " + self.name)
        print("App description: " + self.description)
        print("App githublink: " + self.githublink)
        print("App image: " + self.image)
        print("App Modules: " + self.Modules.value)        

