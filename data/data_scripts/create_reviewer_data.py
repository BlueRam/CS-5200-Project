#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:46:51 2019

@author: Strider
"""

import random 
import numpy as np 
import pandas as pd 

review_qty = .33 * 5000

review_id = range(0, 10000)
userids = range(0, 2480) 
review_user_id = [random.choice(userids) for i in range(10000)]

coffee_id = [1,2,3,4,5,6,7,8,9,10]

cid = [random.choice(coffee_id) for i in range(10000)]

rating_choices = [1,2,3,4,5]
rating_choices_sample = [random.choice(rating_choices) for i in range(10000)]

rating = pd.DataFrame() 
rating['reviewer_id']=review_user_id
rating['coffee_id']=cid
rating['rating']=rating_choices_sample

#print(rating)

rating.to_csv('rating.csv',index=False)
