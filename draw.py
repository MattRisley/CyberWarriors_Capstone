import numpy as np
import pandas as pd
import random as rd

# Calculates random probability

def randomDraw(p):
        n = np.zeros(len(p))
        for i in range(len(p)):
                random_val = rd.uniform(0,1)
                if(random_val< p[i]):
                        n[i] = 1

        return n