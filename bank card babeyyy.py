# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 00:03:34 2023

@author: AlexHP
"""
card = input('Credentials: \n')
error = ("Invalid data!")
if int(len(card)) !=14:
    print (error)
else:
 print ("*" * (len(card)) + card[-4:])
 