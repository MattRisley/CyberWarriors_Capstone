import numpy as np
import decimal
import pandas as pd
import random
from scipy.sparse import lil_matrix, block_diag, csr_matrix

# Generate N x N matrixes
# Number of columns is n
def gen_network(network):
    n = len(network)
    #network = np.random.rand(n, n)
    network = network.round(decimals=2)
    np.fill_diagonal(network, 0)
    #for row in network:
    #    row[::4] =0
    network = np.triu(network, 0) 
    num_Diagonals = 3
    for i in range(n):
            np.fill_diagonal(network[:,(i+num_Diagonals %n):], 0)
    return network
    

def gen_states(n):
    array = np.zeros(n)
    array[0] = 1
    array[1] = 1
   # return np.random.randint(2, size=n)
    return array 

def watch(n):
    watch =  np.random.randint(2, size=n)
    watch[0] = 1
    watch[1] = 1 

    return watch

def CVCMatrix(n):
    #Change file name to accomidate other cvc score files
    #MS10PrivData.csv - Microsoft Windows 10
    
    cvcData = pd.read_csv("MS10PrivData.csv")
    scoreVector = 1- cvcData['Score']*0.10

    network = scoreVector
    network = np.array(network)

    network = np.random.choice(scoreVector, n*n)
    random.shuffle(network)
    network = np.reshape(network, (n,n))

    return gen_network(network)





