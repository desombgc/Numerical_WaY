# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:08:59 2022

@author: Somnath
"""
import numpy as np
p=10**7
square_points=0.0
circle_points=0.0
for i in range (p):
    rand_x=np.random.uniform(-1,1)
    rand_y=np.random.uniform(-1,1)
    origin_dist=rand_x**2+rand_y**2  #distance between (x,y) from origin
    if origin_dist <= 1:
        circle_points=circle_points+1.0
        
    square_points=square_points+1.0
    pi = 4.0*circle_points/square_points
print("value of pi = " , pi) 
print("A= " , circle_points)  #area of the circle 