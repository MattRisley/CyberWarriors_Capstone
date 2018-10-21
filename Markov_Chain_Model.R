print("Hello World")

# Change file path to data 
setwd("~/Google Drive File Stream/Team Drives/CMDA Capstone: Cyber Warriors/Data")
data_1 <-read.csv("MS10PrivData.csv")

#SIR Model?
# Suseptable and Infected Node ->  Suseptable and Infected Node 

#Population and Initial Condition? 
# Probablity 
# inital_1 = 100% infected
# -> next node = 20% prob of getting infected

# Bayesian Statistics Approach
#source("http://bioconductor.org/biocLite.R")
#biocLite(c("graph", "RBGL", "Rgraphviz"))
#install.packages("gRbase", dependencies=TRUE); 
#install.packages("gRain", dependencies=TRUE); 
#install.packages("gRim", dependencies=TRUE)
library(gRain)

data(cad1)
head(cad1, 5)
