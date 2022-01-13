import math


def cdf_normal(x, mu, sigma):
    return 1 / 2 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


cdf_normal_9 = cdf_normal(9, 10, 1)
cdf_normal_12 = cdf_normal(12, 10, 1)
cdf_normal_9_12 = cdf_normal_12 - cdf_normal_9
print(round(cdf_normal_9_12, 4))
