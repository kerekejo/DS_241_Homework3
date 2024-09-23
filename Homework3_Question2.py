import matplotlib.pyplot as plt
import numpy as np


x1 = [1,2,3,4,5]
y1 = [2,4,6,8,10]

x2 = [1,2,3,4,5]
y2 = [7,1,4,2,5]

x3 = [-2,-1,0,1,2]
y3 = [2,1,0,1,2]

x4 = []
y4 = []

def plotDs(dsX, dsY):
    plt.figure(figsize=(8,8))
    plt.scatter(dsX,dsY, color='blue', marker='o')
    plt.title("Scatter Plot for Two Datasets")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def calcCoefficient(dsX,dsY):
    #Error Checking because one of the data sets is empty
    if len(dsX) != len(dsY):
        return 0
    
    if len(dsX) == 0 or len(dsY) == 0:
        return 0
    
    # Calculate the means of X and Y using numpy library
    mean_X = np.mean(dsX)
    mean_Y = np.mean(dsY)
    
    # Calculate the numerator and denominator using numpy library
    numerator = np.sum((dsX - mean_X) * (dsY - mean_Y))
    denominator = np.sqrt(np.sum((dsX - mean_X)**2) * np.sum((dsY - mean_Y)**2))
    
    #More error checking
    if denominator == 0:
        return 0  
    
    correlation_coefficient = numerator / denominator
    return correlation_coefficient

#First Dataset
plotDs(x1,y1)
print("First Dataset: ", calcCoefficient(x1,y1))

#Second Dataset
plotDs(x2,y2)
print("Second Dataset: ", calcCoefficient(x2,y2))

#Third Dataset
plotDs(x3,y3)
print("Third Dataset: ", calcCoefficient(x3,y3))

#Fourth Dataset
plotDs(x4,y4)
print("Fourth Dataset: ", calcCoefficient(x4,y4))