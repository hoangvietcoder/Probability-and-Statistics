import matplotlib.pyplot as plt
import math


def generator_data(a, b, size):
    n = (b - a) / (size - 1)
    result = []
    s = a;
    while s < b:
        result.append(s)
        s = s + n
    if len(result) < size:
        result.append(b)
    return result


def cdf_normal(x, mu, sigma):
    return 1 / 2 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


def plot_cdf_normal(mu, sigma):
    X = generator_data(mu - 4 * sigma, mu + 4 * sigma, 1000)
    P_normal = [cdf_normal(x, mu, sigma) for x in X]
    plt.plot(X, P_normal, '-')
    plt.title('CDF of Normal(%.2f, %.2f)' % (mu, sigma))
    plt.xlabel('X')
    plt.ylabel('P')
    plt.show()


plot_cdf_normal(0, 1.5)
