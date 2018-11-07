import numpy as np
import pandas as pd

def CalculateProb(M,N):
    p = np.zeros(len(N))
    for i in range (0, len(N)):
        
    #if node is already compromised, value will remain 1
    #if no nodes connected to a node are compromised the value will reamain 0
    
        colM = M[:,i]
        initProbs = np.multiply(colM,N)
        oneArray = np.ones(len(N))
        prelimProbs = np.subtract(oneArray,initProbs)
        product = np.prod(prelimProbs)
        finalProb = 1 - product
        p[i] = finalProb
        
    return p
    
    