import matplotlib.pyplot as plt
import math


def pmf_geo(p, x):
    return p * (1 - p) ** x


def plot_pmf_geo(p, n):
    K = list(range(0, n + 1))
    P_geo = [pmf_geo(p, x) for x in K]
    plt.plot(K, P_geo, '-o')
    plt.title('PMF of Geometric(%i, %.2f)' % (p, n))
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()


print(round(pmf_geo(0.4, 2), 3))
plot_pmf_geo(0.4, 10)
