# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 21:35:41 2019

@author: noahd
"""

import pandas as pd
import random

order_id=range(1,3750)
coffee_id=range(1,10)

order_coffee_df=pd.DataFrame()
d=[random.choice(order_id) for i in range(0,5000)]
c=[random.choice(coffee_id) for i in range(0,5000)]
order_coffee_df['order_id']=d
order_coffee_df['coffee_id']=c
order_coffee_df=order_coffee_df.drop_duplicates()
order_coffee_df.to_csv('coffee_order.csv')
print(order_coffee_df['coffee_id'].value_counts())
