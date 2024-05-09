#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 09:43 2023

@author: Samuel L. Smallman
Department of Computer Science
Middle Tennessee State University
Greedy Local search to find max value
of the SoG function in d dimensions.

Portions based on Python code provided by
Scott P. Morton and Joshua L. Phillips
Center for Computational Science
Middle Tennessee State University
"""
import SumofGaussians as SG
import numpy as np
import sys, math
from decimal import Decimal

#Checks if 3 arguments given
#if (len(sys.argv) != 3):
    #print()
    #print("Usage: %s [seed] [dimensions] [Gaussians]")
    #print()
    #sys.exit(1)

#def greedy(sog):

def main():
    s = int(sys.argv[1]) #seed for random generation
    d = int(sys.argv[2]) #dimensions: usually 1 or 2
    n = int(sys.argv[3]) #number of centers
    epsilon = 1e-8       #tolerance within which increase is negligible

    rng = np.random.default_rng(s)
    sog = SG.SumofGaussians(d,n,rng)
    vals = rng.uniform(size = d)

    x = vals * 10.0 # get randomized starting point
  
    for ele in x: #print all coordinates of point x
        print("%.8f"%ele,end = ' ')
    print("%.8f"%sog.Evaluate(x)) #print G(x)
    
    i = 0
    while i < 100000: #program ends at 100,000 iterations 
        step = 0.01 * sog.Gradient(x) #get next step size
        y = x + step #take x up a step
        if (sog.Evaluate(y) <= sog.Evaluate(x)):
            if((Decimal(sog.Evaluate(y)) - Decimal(sog.Evaluate(x))))<=epsilon: #if step doesn't result in significant increase (within epsilon tolerance), likely (local) MAX
                for ele in x: #print all coordinates of point x
                    print("%.8f"%ele,end = ' ')
                print("%.8f"%sog.Evaluate(x)) #print G(x)
                break
        x = y #get new position
        for ele in x: #print all coordinates of point x
            print("%.8f"%ele,end = ' ')
        print("%.8f"%sog.Evaluate(x)) #print G(x)
        i += 1
    
   
main()
#math.isclose(sog.Evaluate(neighbor),sog.Evaluate(x), rel_tol=epsilon) or #TEST
# 0 2 50 -> 5.91439213 3.37653658 4.34235761
# 0 1 20 -> 0.28260433 4.02185099