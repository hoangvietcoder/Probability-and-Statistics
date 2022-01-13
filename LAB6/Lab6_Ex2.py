import matplotlib.pyplot as plt
import math


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def pmf_poisson(k, lam):
    return ((lam ** k) * (math.exp(-lam))) / factorial(k)


def plot_pmf_poisson(n, lam):
    K = list(range(0, n + 1))
    P_poisson = [pmf_poisson(k, lam) for k in K]
    plt.plot(K, P_poisson, '-o')
    plt.title('PMF of Poisson(%i)' % lam)
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()


print(round(pmf_poisson(2, 3), 3))
plot_pmf_poisson(5, 3)
