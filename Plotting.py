#Matrix Plot 
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def plotMatrix(M):

    G = nx.from_numpy_matrix(np.array(M)) 
    nx.draw(G, with_labels=True, node_color='r')
    plt.show()

def barChart(steps_vector):

    plt.hist(steps_vector)
    plt.show()