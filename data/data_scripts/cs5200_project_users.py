# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:39:43 2019

@author: noahd
"""

from faker import Faker
fake=Faker()
import pandas as pd
from random import randint      # For student id 
import json 



student_data={}
for i in range(0,5000):
    student_data[i]=fake.profile()
    
s=pd.DataFrame.from_dict(student_data,orient='index')

s.to_csv('users.csv')