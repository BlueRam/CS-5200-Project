# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:30:09 2019

@author: noahd
"""

import pandas as pd 
import random
farmers=pd.read_csv("C:/Users/noahd/Music/coffee_farmer.csv")
farmers_final=farmers[[ 'Operation Name']].dropna()
origins=farmers[[ 'Physical Address: State/Province',
       'Physical Address: Country']].dropna()

origins.columns=['state','Country']
x=range(0,origins.shape[0])
origins['origin_id']=x

place=[]
for i in range(0,farmers_final.shape[0]):
    y=random.randint(0,len(x)-1)
    v=x[y]
    place.append(v)
    
    
place=pd.DataFrame(place)
farmers_final['origin_id']=place[0]


farmers_final.to_csv('farmers.csv',index=False)
origins.to_csv('origin.csv',index=False)

