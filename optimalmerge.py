

#program for finding cost for optimal merge pattern

def optimized_cost(weights):

    length=len(weights)
    temp=[]
    for i in range(length):
        weights=sorted(weights)
        print("\nSizes\n",weights)
        if len(weights)>1:
            temp.append(weights[0]+weights[1])
            weights.append(weights[0]+weights[1])
            for j in range(2):
                weights.pop(0)
    print("\ncost path",temp)
    return sum(temp)

if __name__ == "__main__":
    weights=list(map(int,input("Enter Sizes with spaces : ").split()))
    print("\nCost is",optimized_cost(weights))