import numpy as np
import matplotlib.pyplot as plt
import scipy
import random
from scipy import stats

def sigma_z_table_verification():
    sigmaValues=[0,.1,.2,.3,.4,.5,.6,.7,.8,.9]
    probabilityValues = []
    for sigma in sigmaValues:
        probability = stats.norm.cdf(sigma)
        probabilityValues.append(probability)
        print(probability)
     
    return probabilityValues
#stats.norm.rvs
def probability_z_table_verification(probabilityValues):
    for probability in probabilityValues:
        sigmaValues = stats.norm.ppf(probability)
        print(sigmaValues)

def rayleigh_dist():
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(stats.rayleigh.ppf(0.01),stats.rayleigh.ppf(0.99), 100)
    ax.plot(x, stats.rayleigh.pdf(x),'r-', lw=5, alpha=0.6, label='rayleigh pdf')
    rv = stats.rayleigh()
    vals = stats.rayleigh.ppf([0.001, 0.5, 0.999])
    r = stats.rayleigh.rvs(size=100000)
    ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
    ax.legend(loc='best')
    plt.show()

def main():
    p = sigma_z_table_verification()
    probability_z_table_verification(p)
    rayleigh_dist()


if __name__ == '__main__':
    main()
