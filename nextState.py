from cond import CalculateProb
from draw import randomDraw


#Calculate Probabilities and update N for next step
def state_n(M, N):
    p = CalculateProb(M,N)
    print(p)

    for i in range(len(p)):
        if(N[i] != 1):
            N[i] = p[i]
    N = randomDraw(N)
    print("Next Comprosied State: ", N)