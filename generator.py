import numpy as np
import decimal
import pandas as pd
import random
from scipy import sparse
from scipy.sparse import lil_matrix, block_diag, csr_matrix, csc_matrix

'''
Generate Matrix Network with some Diagonals Filled

def gen_network(network):
    
    Use for Random network
    n is the number of columns
    network = np.random.rand(n, n)
    
    n = len(network)
    network = network.round(decimals=2)
    np.fill_diagonal(network, 1)
    network = np.triu(network, 0) 
    num_Diagonals = len(str(n)) + 1
    for i in range(n):
            np.fill_diagonal(network[:,(i+num_Diagonals %n):], 0)
    return network

'''
''' Generate the initial state matrix with first two  '''
def gen_states(n):
    array = np.zeros(n)
    array[0] = 1
    array[1] = 1
    return array

'''
Randomly generates the compromised states vector
Create a list of nodes that the User wants to watch for compromise. 
'''
def watch(n):
    watch =  np.random.randint(2, size=n)
    watch[0] = 1
    watch[1] = 1 
    return watch

''' 
Pull Score data from CVC Data

Read in csv of conditional matrix here. Conditional Matrix contains likelihood 
that ohter nodes will be infected given an initial condition that represents 
which nodes are already compromised. 

Change file name to accomidate other cvc score files
MS10PrivData.csv - Microsoft Windows 10
'''
def CVCMatrix(n):

    cvcData = pd.read_csv("MS10PrivData.csv")
    scoreVector = 1- cvcData['Score']*0.10

    #Creates the random indices (row, col) for were to place data
    row = np.random.uniform(0,n-1, n*int(n/3))
    row = np.around(row)

    col = np.random.uniform(0,n-1, n*int(n/3))
    col = np.around(col)

    data = np.random.choice(scoreVector, n*int(n/3))

    #Shuffles data around to add randomization 
    random.shuffle(data)
    #Make a sparse matrix
    smatrix = sparse.coo_matrix((data,(row,col)),shape=(n,n)).tocsr()
    network = smatrix.toarray()

    #Organize data 
    np.fill_diagonal(network, 1)
    for i in range(n):
        np.fill_diagonal(network[:,1:], data)
    network = np.triu(network, 0) 

    #gen_network(network)

    return network





