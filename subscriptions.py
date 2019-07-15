# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:43:12 2019

@author: noahd
"""

import pandas as pd
import random
from faker import Faker
fake = Faker()
h=fake.date_time_between(start_date='-30y', end_date='now')
# datetime.datetime(2007, 2, 28, 11, 28, 16)
h=[fake.date_time_between(start_date='-30y', end_date='now') for i in range(0,3750)]
sub_id=range(0,3750)
userids=range(0,5000)
sub_user_id=random.sample(userids,3750)
membership=['small','medium']
subscription=pd.DataFrame()
subscription['date_subscribed']=h
subscription['subscription_id']=sub_id
subscription['user_id']=sub_user_id

d=[random.choice(membership) for i in range(3750)]
subscription['membership']=d
subscription.to_csv('subscription.csv',index=False)