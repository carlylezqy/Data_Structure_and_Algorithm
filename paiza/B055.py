import math
import numpy as np

def main(fare_rules, X):
    fare_rules = np.array(fare_rules)
    fares = []

    for i in fare_rules:
        if(X - i[0] >= 0):
            fares.append(i[1] + math.ceil((X - i[0] + 1) / i[2]) * i[3])
        else:
            fares.append(i[1])
    
    print(min(fares), max(fares))

if __name__ == '__main__':
    N, X = input().split(' ')
    fare_rules = []
    for i in range(int(N)):
        fare_rules.append(list(map(int, input().split(' '))))

    main(fare_rules, int(X))