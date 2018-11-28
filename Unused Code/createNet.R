createNet <- function(r,c){
  r = as.integer(r)
  c = as.integer(c)
  net <- matrix( rep( 0, len=r), ncol = c, nrow = r)
  for (i in 1:r){
    for (j in 1:c){
      if (i != j){
        net[i,j] <- runif(n = 1, min = 0, max = 1)
      }
    }
  }
  return(net)
  write.csv(net, '~/Documents/network.csv')
}
