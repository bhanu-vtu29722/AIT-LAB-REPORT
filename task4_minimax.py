
def minimax(depth,nodeIndex,isMax,scores,alpha,beta,height):
    if depth==height:
        return scores[nodeIndex]
    if isMax:
        best=float("-inf")
        val=minimax(depth+1,nodeIndex*2,False,scores,alpha,beta,height)
        best=max(best,val)
        alpha=max(alpha,best)
        if beta<=alpha:
            return best
        val=minimax(depth+1,nodeIndex*2+1,False,scores,alpha,beta,height)
        best=max(best,val)
        alpha=max(alpha,best)
        return best
    else:
        best=float("inf")
        val=minimax(depth+1,nodeIndex*2,True,scores,alpha,beta,height)
        best=min(best,val)
        beta=min(beta,best)
        if beta<=alpha:
            return best
        val=minimax(depth+1,nodeIndex*2+1,True,scores,alpha,beta,height)
        best=min(best,val)
        beta=min(beta,best)
        return best
if __name__=="__main__":
    scores=[3,6,6,9,5,2,4,-1,3,5,6,9,3,7,0,-1]
    import math
    height=int(math.log(len(scores),2))
    print("opotimal value fro max player:",minimax(0,0,True,scores,float("-inf"),float("inf"),height))

            
