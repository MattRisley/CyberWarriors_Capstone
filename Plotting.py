#Matrix Plot 
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns
from scipy import stats


''' Visualize M Matrix using the networkx library'''
def plotMatrix(M,Watch):
    plt.figure(figsize=(13,6))
    
    G = nx.from_numpy_matrix(np.array(M)) 
    pos = nx.spring_layout(G)

    colormap = []
    for i in range(len(M)):
        if(i <2):
            colormap.append('red')
        else:
            colormap.append('green')

    plt.subplot(1,3,1)
    nx.draw(G, with_labels=True, node_color=colormap, node_size=400, 
    edge_color='black', linewidths=1, font_size=15, pos = pos)
    plt.figtext(0.15, 0.95, "Initial Network")

    colormap = []
    for i in range(len(M)):
        if(Watch[i] == 1):
            colormap.append('red')
        else:
            colormap.append('green')

    


    plt.subplot(1,3,3)
    nx.draw(G, with_labels=True, node_color=colormap, node_size=400, 
    edge_color='black', linewidths=1, font_size=15, pos = pos)
    plt.figtext(0.8, 0.95, "Compromised Network")
    


''' Generate Bar Chart based off the steps taken'''
def barChart(steps_vector):

    #plt.subplot(1,3,2)
    plt.hist(steps_vector, density=1)
    sns.distplot(steps_vector, hist= False)
    
    plt.title("Number of Steps Taken Across Multiple Iterations")
    plt.xlabel("Number Steps Taken")
    plt.ylabel("Number of Interations")


    ## Add Descriptive Statistics
    n, min_max, mean, var, skew, kurt = stats.describe(steps_vector)
    sd = np.std(steps_vector)
    vector_mode = stats.mode(steps_vector)
    descriptiveStats = "Number of elements: {0:d}".format(n) + "\n" + "Minimum: {0:d}".format(min_max[0]) + "\n" + "Maximum: {0:d}".format(min_max[1]) + "\n" + "Mean: {0:4.3f}".format(mean) + "\n" + "Mode: {0:d}".format(vector_mode[0][0]) + "\n" + "Variance: {0:4.3f}".format(var) + "\n" + "Standard Deviation: {0:4.3f}".format(sd)

    plt.figtext(0.65, 0.65, descriptiveStats)
    
    plt.tight_layout()

    plt.savefig('Network.png', bbox_inches='tight')

