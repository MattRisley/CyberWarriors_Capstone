import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cond import CalculateProb
from draw import randomDraw
import random as rd
from generator import gen_network
from generator import gen_states
from generator import watch
from generator import CVCMatrix
import Plotting 

from joblib import Parallel, delayed
import multiprocessing
import warnings
import sys
import warnings



def main(M, N, interations):

    #PS, EA, MR
    #read in csv of conditional matrix here. Conditional Matrix contains likelihood that ohter nodes will be infected given
    #an initial condition that represents which nodes are already compromised. Initial condition(s) are in the csv.

    #seperate out M, the probability matrix, and N the Node matrix
    #M = gen_network(size)
    initN = N


    #Create a list of nodes that the User wants to watch for compromise. 
    #This list will determine how long the simulation will run. 
    Watch = watch(size)
    print("Watch Vector:", Watch)
    # Checks to see if the nodes in watch are compromised or not. Returns a boolean.

    # Parallize
    num_steps = []
    num_cores = multiprocessing.cpu_count()
    num_steps = Parallel(n_jobs=num_cores)(delayed(parallel_section)(initN, Watch) for i in range(iterations))
    return num_steps
    
def parallel_section(initN, Watch):
    
    N = initN
    count = 0
    while(not isCompromised(Watch, N)):
        p = CalculateProb(M,N)
        for j in range(len(p)):
            if(N[j] != 1):
                N[j] = p[j]
        N = randomDraw(N)
        count = count + 1
    return count


def isCompromised(Watch , N):
        watch_ones = np.where(np.array(Watch) == 1)
        N_ones = np.where(np.array(N) == 1)
        return set(watch_ones[0]).issubset(set(N_ones[0]))

if __name__ == '__main__':

    warnings.simplefilter("ignore")
    warnings.filterwarnings("ignore")

    print("Running Simulation \n")
    size = int(input("Input Matrix Size for n x n: "))
    iterations = int(input("Input the number of iterations you'd like to run: "))

    M = CVCMatrix(size)
    N = gen_states(size)
    iterations = size
    print(M)
    print(N)
    agents = 5
    chunksize = 3
    
    num_steps = main(M, N, iterations)

    print("Number of Steps Taken: ", num_steps)

    Plotting.plotMatrix(M)
    Plotting.barChart(num_steps)
    print("\n")
    print("Simulation Complete")



