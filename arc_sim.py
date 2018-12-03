import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt

import sys
import warnings
import Plotting 
import multiprocessing
from draw import *
from cond import *
from saveFile import *
from generator import * 
from joblib import Parallel, delayed
#from draw import randomDraw
#from cond import CalculateProb
#from joblib import Parallel, delayed
#from generator import gen_states
#from generator import watch
#from generator import CVCMatrix


'''
Generate a Watch Vector for stopping conditions
Run Parallel Processes to determine number of steps until compromised state
'''
def main(M, N, interations):
    
    initN = N
   
    #This list will determine how long the simulation will run. 
    Watch = watch(size)
    print("Watch Vector:", Watch)

    #Parallel process based off number of cores
    num_steps = []
    num_cores = multiprocessing.cpu_count()
    num_steps = Parallel(n_jobs=num_cores)(delayed(parallel_section)(initN, Watch) for i in range(iterations))
    return num_steps, Watch
    

'''Parallelization Of Computing steps for Compromised Network'''
def parallel_section(initN, Watch):
    
    N = initN
    count = 0
    # Checks to see if the nodes in watch are compromised or not. Returns a boolean.
    while(not isCompromised(Watch, N)):
        p = CalculateProb(M,N)
        for j in range(len(p)):
            if(N[j] != 1):
                N[j] = p[j]
        N = randomDraw(N)
        count = count + 1
    return count

'''Watches for Comprised State'''
def isCompromised(Watch , N):
        watch_ones = np.where(np.array(Watch) == 1)
        N_ones = np.where(np.array(N) == 1)
        return set(watch_ones[0]).issubset(set(N_ones[0]))


'''Initalization and Running'''
if __name__ == '__main__':

    warnings.simplefilter("ignore")
    warnings.filterwarnings("ignore")

    #print("Running Simulation \n")
    #size = int(input("Input Matrix Size for n x n: "))
    #iterations = int(input("Input the number of iterations you'd like to run: "))
    size = 30000
    iterations = 1000
    

    # Generate M matrix and N vector
    M = CVCMatrix(size)
    N = gen_states(size)
    print(M)
    print(N)
    
    num_steps, Watch  = main(M, N, iterations)
    save(num_steps)
    print(num_steps)
    print ("Done")





