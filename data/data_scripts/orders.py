# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 21:03:58 2019

@author: noahd
"""

import pandas as pd
import random

order_id=range(0,3751)
userids=range(0,5000)

subscription_order = [1,0]
subscription_samples = [random.choice(subscription_order) for i in range(0,3751)]

order_df=pd.DataFrame()
d=[random.choice(userids) for i in order_id]
order_df['order_id']=order_id


from random import randint
import datetime

dd=[datetime.date(randint(2018,2019), randint(1,12),randint(1,28)) for i in order_id]

order_df['subscription_order'] = subscription_samples
order_df['order_date']=dd
order_df['user_id_o']=d
order_df.to_csv('order.csv')

print(order_df)