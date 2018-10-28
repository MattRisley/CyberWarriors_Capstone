import numpy as np
import pandas as pd
import random as rd

def randomDraw(p):
    n = np.zeros(len(p))
    for i in range(0,len(p)):        
        if (rd.uniform(0,1) < p(i)):
            n[i] = 1

    return n