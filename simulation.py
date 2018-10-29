import numpy as np
import pandas as pd
from cond import CalculateProb
#PS, EA, MR
#read in csv of conditional matrix here. Conditional Matrix contains likelihood that ohter nodes will be infected given
#an initial condition that represents which nodes are already compromised. Initial condition(s) are in the csv.
conditional  =  pd.read_csv("net.csv")
print(conditional)
#seperate out M, the probability matrix, and N the Node matrix
numCol = len(conditional.columns)
M = np.array(conditional.iloc[0:numCol])
N = np.array(conditional.iloc[0:numCol])


#Create a list of nodes that the User wants to watch for compromise. 
#This list will determine how long the simulation will run. 

Watch = N[5].tolist()
print (Watch)