import matplotlib.pyplot as plt
import math


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def pmf_binom(k, n, p):
    return ((factorial(n)) / ((factorial(k)) * (factorial(n - k)))) * (p ** k) * ((1 - p) ** (n - k))


def plot_pmf_binom(n, p):
    K = list(range(0, n + 1))
    P_binom = [pmf_binom(k, n, p) for k in K]
    plt.plot(K, P_binom, '-o')
    axes = plt.gca()
    axes.set_xlim([0, n])
    axes.set_ylim([0, 1.1 * max(P_binom)])
    plt.title('PMF of Bin(%i, %.2f)' % (n, p))
    plt.xlabel('Number k of successes')
    plt.ylabel('Probability of k successes')
    plt.show()


print(round(pmf_binom(2, 5, 0.1), 3))
plot_pmf_binom(5, 0.1)
