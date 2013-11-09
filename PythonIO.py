# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Standard User\.spyder2\.temp.py
"""
import numpy as np
import csv
import time
from sklearn import cross_validation
from sklearn.metrics import make_scorer

traindata = []
file_name = "C:/Users/Standard User/Downloads/train.csv"
reader = csv.DictReader(open(file_name, 'rb'), delimiter=',', quotechar='"')
for row in reader:
    traindata.append(row)

for sub in traindata:
    for key in sub:
        if key == 'id' or key == 'num_votes' or key == 'num_comments' or key == 'num_views':
            sub[key] = int(sub[key])
        elif key == 'latitude' or key =='longitude':
            sub[key] = float(sub[key])
        elif key == 'created_time':
            sub[key] = time.mktime(time.strptime(sub[key], "%Y-%m-%d %H:%M:%S"))    # make time into datetime (float)

testdata = []
file_name = "C:/Users/Standard User/Downloads/test.csv"
reader = csv.DictReader(open(file_name, 'rb'), delimiter=',', quotechar='"')
for row in reader:
    testdata.append(row) 
    
for sub in testdata:
    for key in sub:
        if key == 'id' or key == 'num_votes' or key == 'num_comments' or key == 'num_views':
            sub[key] = int(sub[key])
        elif key == 'latitude' or key =='longitude':
            sub[key] = float(sub[key])
        elif key == 'created_time':
            sub[key] = time.mktime(time.strptime(sub[key], "%Y-%m-%d %H:%M:%S"))
            
print testdata[id]
