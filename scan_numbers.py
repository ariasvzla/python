#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 09:26:50 2018

@author: elian
"""
a=[2,3,4,5,6,7,5,5]
x=[]
userin=int(input("please enter a number: "))
for scan in a:
        if scan<userin:
            print(scan, "is less than " +str(userin))
        else:
            x.append(scan)
print("numbers equal or greater than " +str(userin)+ " : "+ str(x))
    
    