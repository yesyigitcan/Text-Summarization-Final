'''
import numpy as np
a = [(1, 2),(2,4)]
print(list(set(np.ravel(a))))
'''
from collections import Counter
from statistics import mode, mean, median, quantiles, median_high


a = ["a", "a", "c","c", "c","c", "d", "c", "b", "c", "c", "c", "d", "c", "c", "c", "c", "c", "c", "e"]
a_c = Counter(a)
print(a_c)
print(a_c.values())
m = mean(a_c.values())
med = median(a_c.values())
q = quantiles(a_c.values())
q_up = q[2]
med_up = median_high(a_c.values())
print(m)
print(med)
print(q_up)
print(q)
print(med_up)

if m > med_up:
    for key in a_c.keys():
        if a_c[key] > med_up:
            print("Value {} penalty score is {}".format(a_c[key], med_up/a_c[key]))