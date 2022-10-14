

#program for finding cost for optimal merge pattern

#function to calculate optimal cost
def optimized_cost(weights):

    length=len(weights)
    #list for path/parent node
    temp=[]
    
    for i in range(length):
        weights=sorted(weights)
        print("\nSizes\n",weights)
        if len(weights)>1:
            #merge minimum weight pair and add to both list and finally pop the pair out.
            temp.append(weights[0]+weights[1])
            weights.append(weights[0]+weights[1])
            for j in range(2):
                weights.pop(0)
    print("\ncost path",temp)
    #return cost
    return sum(temp)

if __name__ == "__main__":
    weights=list(map(int,input("Enter Sizes with spaces : ").strip().split()))
    print("\nCost is",optimized_cost(weights))
