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
h=[fake.date_time_between(start_date='-30y', end_date='now') for i in range(0,3751)]
sub_id=range(0,3751)
userids=range(0,5000)
sub_user_id=random.sample(userids,3751)
membership=['Gold','Silver','Bronze']
subscription_levels = [1,2,3]
subscription_levels_sample = [random.choice(subscription_levels) for i in range(0,3751)]


subscription=pd.DataFrame()

subscription['subscription_id']=sub_id
subscription['date_subscribed']=h

d=[random.choice(membership) for i in range(3751)]
subscription['membership']=d

subscription['user_id']=sub_user_id


subscription['level_id'] = subscription_levels_sample 
subscription.to_csv('subscription.csv',index=False)
