#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:56:17 2021

@author: TetonRetinalInstitute
"""


class Board:
    def __init__(self):
    def parsing(self, command):
        if(len(command) != 2):
            return "invalid move you fool"
        else:
            x = command[0]
            y = command[1]
            
            if(x is in ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H"]):
                x = x.lower() #make a case (fancy if else) where a or A = 1, b or B = 2 etc. 
            else return "Invalid command foo"
            if(y is in ["1", "2", "3", "4", "5", "6", "7", "8"]):
                y = int(y)
            else return "you ever played chess before? n00b"
            
            
            
         
         
        