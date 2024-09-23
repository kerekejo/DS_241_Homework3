import numpy as np
from statistics import multimode

ds = [5,7,8,5,10,12,7,6]

#Calculate the mean
def calculate_mean(numbers):
    if len(numbers) == 0:
        return 0 
    return sum(numbers) / len(numbers)

#Find the 25th and the 75th percentile
def calculate_percentiles(data):
    q1 = float(np.percentile(data, 25))
    q3 = float(np.percentile(data, 75))
    
    return q1, q3  

def calculate_modes(data):
    modes = multimode(data)
    return modes
    
print("Mean: ",calculate_mean(ds))
print("Percentiles: ", calculate_percentiles(ds))
print("Modes: ", calculate_modes(ds))