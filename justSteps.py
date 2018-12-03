
from Plotting import *

openfile = open("n_steps_MS10PrivData.txt", 'r')

array =  openfile.read().splitlines()
results = list(map(int, array))

barChart(results)
