import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cond import CalculateProb
from draw import randomDraw
import random as rd
from generator import gen_network
from generator import gen_states
from generator import watch

#PS, EA, MR
#read in csv of conditional matrix here. Conditional Matrix contains likelihood that ohter nodes will be infected given
#an initial condition that represents which nodes are already compromised. Initial condition(s) are in the csv.
conditional  =  pd.read_csv("net1.csv")
size = 100
#seperate out M, the probability matrix, and N the Node matrix
numCol = len(conditional.columns)
M = gen_network(size)
N = gen_states(size)
print(M)
print(N)
initN = N




#Create a list of nodes that the User wants to watch for compromise. 
#This list will determine how long the simulation will run. 
Watch = watch(size)
print("Watch Vector:", Watch)
# Checks to see if the nodes in watch are compromised or not. Returns a boolean.
def isCompromised():
    count = 0
    watch_ones = np.where(np.array(Watch) == 1)
    N_ones = np.where(np.array(N) == 1)
    return set(watch_ones[0]).issubset(set(N_ones[0]))


n = 10 # Number of iterations
num_steps = []
for i in range(n):
    #print("Interation: ", i)
    N = initN
    count = 0
    while(not isCompromised()):
        p = CalculateProb(M,N)
        for j in range(len(p)):
            if(N[j] != 1):
                N[j] = p[j]
        #print("Next Step Prob:", p)
        N = randomDraw(N)
        count = count + 1
    num_steps.append(count)
    #print("Number of Steps Taken: ", num_steps[len(num_steps)-1])
    #print("N vector: ", N)
    #print("")
print("Number of Steps Taken: ", num_steps)







