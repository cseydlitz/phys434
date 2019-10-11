# Still need to do this mathematically
# How to get proper y scale?
import numpy as np
import matplotlib.pyplot as plt
import random

rolls=[]
def main():
    for i in range(1,10000):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        sum = d1+d2
        rolls.append(sum)
    plt.hist(rolls)
    plt.show()

if __name__ == '__main__':
    main()
