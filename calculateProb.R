## Calculating Probability

calculateProb <- function(M, N){
  
  p = rep(0,length(N))
  for(i in length(N)){
    
    colM = M[,1]
    initProb = colM * N
    oneArray = rep(1, length(N))
    prelimProbs = oneArray - initProb
    product = prod(prelimProbs)
    finalProb = 1- product
    p[i] = finalProb
  }
  
  p
  
}