#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 10:04 2023

Simulated Annealing to find max value
of the SoG function in d dimensions.

Portions based on Python code provided by
Scott P. Morton and J. Phillips
"""
import SumofGaussians as SG
import numpy as np
import sys

#Checks if 3 arguments given
#if (len(sys.argv) != 3):
    #print()
    #print("Usage: %s [seed] [dimensions] [Gaussians]"))
    #print()
    #sys.exit(1)

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
    print("%.8f"%sog.Evaluate(x))
    t = 1 #starting temperature (linear)
    #t = 100000 #starting temperature (non-linear)
    i = 100000
 
    while i > 0:
        step =  rng.uniform(low = -0.05, high = 0.05, size = d) #get random next step size in range -0.05 to 0.05
        y = x + step #take x up a step
        if sog.Evaluate(y) > sog.Evaluate(x):
            x = y
        else:
            if rng.uniform(low = 0, high = 1) < np.exp((sog.Evaluate(y) - sog.Evaluate(x))/t): #random num [0-1] < probability  e ** ((G(y)-G(x))/t)
                #print(math.exp((sog.Evaluate(y) - sog.Evaluate(x))/t)) #probability test, currently trends higher than I'd like
                x = y
        t -= 0.00001 #Annealing Schedule (linear)
        #t = t**(-t)#(t ** (1. / 3))#np.sqrt(t) #Annealing Schedule (non-linear); try log and sq,cb,etc root variants
        if t == 0:
            t+= epsilon
        i -= 1
        for ele in x: #print all coordinates of point x (indent for turn in)
            print("%.8f"%ele,end = ' ')
        print("%.8f"%sog.Evaluate(x)) #print G(x)

main()
# 0 2 50 -> 1.22685355 7.32838845 2.56947819 #TEST
# 0 1 20 -> 
