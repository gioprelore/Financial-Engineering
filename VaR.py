import numpy as np
import csv



# Historical method

print('\n Historical method:')
#We open the file
with open(r'C:\Users\George\Documents\Berkeley 2018-2019\Fall Semester\Elective\IND 221 Introduction to Financial Engineering\Assignment 4\^DJI.csv', newline = '') as file :
    reader = csv.reader(file)
    M = list(reader)
    #We delete the first line of the file because it contains only text
    L = M[1:]       
    l = len(L)
    #We create an empty list that would be implemented with the losses
    Loss1 = []      
    for i in range(0,l-1) :
        a = L[i][4]
        b = L[i+1][4]
        c = float(a)
        d = float(b)
        loss = c-d
        Loss1.append(loss)
    loss1 = len(Loss1)
    #We order the list of the losses
    Loss2 = sorted(Loss1)
    loss2 = len(Loss2)
    #We look for the value that is superior to 99% of all the losses
    a = int(0.99 * loss2)
    VaR = Loss2[a]
    print('\n VaR = ',VaR)



# Parametric method

print('\n \n \n Parametric method:')
#We open the file
with open(r'C:\Users\George\Documents\Berkeley 2018-2019\Fall Semester\Elective\IND 221 Introduction to Financial Engineering\Assignment 4\^DJI.csv', newline = '') as file :
    reader = csv.reader(file)
    M = list(reader)
    L = M[1:]
    l = len(L)
    #We create a list Rx which would be implemented 
    Rx = []
    for i in range(0,l-1) :
        a = L[i][4]
        b = L[i+1][4]
        c = float(a)
        d = float(b)
        r = (d-c)/c
        Rx.append(r)
    rx = len(Rx)
    #We calculate mu
    a = 0
    for i in range(0,rx) :
        a = a + Rx[i]
    mu = a/rx
    print('\n mu =',mu)
    #We calculate sigma
    b = 0
    for i in range(0,rx):
        b = b + (Rx[i]-mu)**2
    SigmaSquare = b/(rx-1)
    sigma = SigmaSquare**(0.5)
    print('\n Sigma =',sigma)
    #We calculate the VaR
    a = float(L[l-1][4])
    VaR = a * (2.33 * sigma - mu)
    print('\n VaR =',VaR)