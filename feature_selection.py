#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 22:23:54 2019

@author: sohel
"""

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

class selector(object):
    
    def __init__(self):
        pass
    
    def select(self,x,y,n):
        slt=SelectKBest(score_func=chi2,k=n)
        best=slt.fit(x,y)
        return(best)
        
    def __del__(self):
        pass