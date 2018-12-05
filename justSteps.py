
from Plotting import *

openfile = open("n_steps_MacOSPrivData.txt", 'r')

array =  openfile.read().splitlines()
results = list(map(int, array))

barChart(results)
