import numpy as np
import decimal
import pandas as pd
from scipy.sparse import lil_matrix, block_diag, csr_matrix

# Generate M x N matrixes
'''
n = 10
network = np.random.rand(n, n)
network = network.round(decimals=2)
np.fill_diagonal(network, 0)
network = np.triu(network, 0) 
np.fill_diagonal(network[:,4:], 0)
np.fill_diagonal(network[:,5:], 0)
np.fill_diagonal(network[:,6:], 0)
print(network)  

'''

# Number of columns is n
def gen_network(n):

    network = np.random.rand(n, n)
    network = network.round(decimals=2)
    np.fill_diagonal(network, 0)
    #for row in network:
    #    row[::4] =0
    network = np.triu(network, 0) 

    for i in range(n):
            np.fill_diagonal(network[:,(i+5 %n):], 0)
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