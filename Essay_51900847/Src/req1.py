#Hàm statistics.mean(data)
import statistics
data1 = [761, 471, 933, 643, 827]
print("Result:" ,statistics.mean(data1))

# #Hàm statistics.fmean(data)
data2 = [466, 47, 705, 990, 875]
print("Result:", statistics.fmean(data2))

#Hàm statistics.geometric_mean(data)
data3 = [86, 211, 868, 666, 121]
print("Result:", statistics.geometric_mean(data3))

#Hàm statistics.harmonic_mean(data)
data4 = [675, 407, 965, 640, 298]
print("Result:", statistics.harmonic_mean(data4))

# #Hàm statistics.median(data)
data5 = [692, 923, 537, 346, 170]
print("Result:", statistics.median(data5))

#Hàm statistics.median_low(data)
data6 = [688, 278, 151, 668, 287]
print("Result:", statistics.median_low(data6))

#Hàm statistics.median_high(data)
data7 = [163, 446, 279, 168, 475]
print("Result:", statistics.median_high(data7))

#Hàm statistics.median_grouped(data, interval=1)
data8 = [548, 494, 61, 360, 863]
print("Result:", statistics.median_grouped(data8, interval = 1))

#Hàm statistics.mode(data)
data9 = [213, 509, 339, 213, 804]
print("Result:", statistics.mode(data9))

#Hàm statistics.multimode(data)
data10 = [199, 336, 747, 818, 199]
print("Result:", statistics.multimode(data10))

#Hàm statistics.quantiles(data, *, n=4, method = ‘exclusive’)   
data11 = [945, 612, 749, 936, 723]
print("Result:", statistics.quantiles(data11, n = 5))

#Hàm statistics.pstdev(data, mu = None)
data12 = [290, 161, 298, 965, 138]
print("Result:", statistics.pstdev(data12))

#Hàm statistics.pvariance(data, mu = None)
data13 = [678, 909, 50, 895, 622]
print("Result:", statistics.pvariance(data13))

#Hàm statistics.stdev(data, xbar = None)
data14 = [275, 263, 56, 36, 37]
print("Result:", statistics.stdev(data14))

#Hàm statistics.variance(data, xbar = None)
data15 = [435, 82, 695, 574, 718]
print("Result:", statistics.variance(data15))