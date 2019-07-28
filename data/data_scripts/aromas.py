# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:55:53 2019

@author: noahd
"""

aromas=pd.DataFrame()

thesmells=["Fruity",
"Berry",
"Strawberry",
"Raspberry",
"Blueberry",
"Blackberry",
"Dried Fruit",
"Raisin",
"Prune",
"Apple",
"Pear",
"Peach",
"Grape",
"Cherry",
"Pomegranate",
"Coconut",
"Pineapple",
"Citrus fruit",
"Lemon",
"Grapefruit",
"Orange",
"Lime",
"Alcohol",
"Whiskey",
"Winey",
"Fermented",
"Olive Oil",
"Raw",
"Under–ripe",
"Peapod",
"Green",
"Fresh",
"Dark Green",
"Vegetative",
"Hay-like",
"Herb-like",
"Beany",
"Musty/earthy",
"Musty/dusty",
"Moldy/damp",
"Phenolic",
"Animalic",
"Meaty/brothy",
"Woody",
"Tobacco",
"Pipe tobacco",
"Acrid",
"Ashy",
"Burnt",
"Smoky",
"Roasted",
"Brown",
"Floral",
"Rose",
"Jasmine",
"Chamomile",
"Black tea",
"Pungent",
"Pepper",
"Anise",
"Nutmeg",
"Brown spice",
"Cinnamon",
"Clove",
"Sweet",
"Molasses",
"Maple Syrup",
"Brown sugar",
"Caramelized",
"Chocolate",
"Cocoa",
"Dark Chocolate",
"Honey",
"Vanilla"]
aromas['flavor_aroma_description']=thesmells

aromas['flavor_aroma_id']=range(0,len(thesmells))
aromas.to_csv('aromas.csv',index=False)


aromas_coffee=pd.DataFrame()
d=[random.choice(range(1,11)) for i in range(150)]
a=[random.choice(range(1,74)) for i in range(150)]

aromas_coffee['flavor_aroma_id']=a
aromas_coffee['coffee_id']=d
aromas_coffee.to_csv("aromas_coffee.csv")