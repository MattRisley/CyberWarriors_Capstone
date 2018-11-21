#Matrix Plot 
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns


''' Visualize M Matrix using the networkx library'''
def plotMatrix(M):

    G = nx.from_numpy_matrix(np.array(M)) 
    nx.draw(G, with_labels=True, node_color='red', node_size=400, 
    edge_color='black', linewidths=1, font_size=15)
    plt.show()

''' Generate Bar Chart based off the steps taken'''
def barChart(steps_vector):

    plt.hist(steps_vector, density=1)
    sns.distplot(steps_vector, hist= False)
    
    plt.title("Number of Steps Taken Across Multiple Iterations")
    plt.xlabel("Number Steps Taken")
    plt.ylabel("Number of Interations")

    plt.show()