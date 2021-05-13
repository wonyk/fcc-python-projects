import numpy as np

def getMean(arr):
    return [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr.flat)]

def getVariance(arr):
    return [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr.flat)]

def getStdDev(arr):
    return [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr.flat)]

def getMin(arr):
    return [np.amin(arr, axis=0).tolist(), np.amin(arr, axis=1).tolist(), np.amin(arr.flat)]

def getMax(arr):
    return [np.amax(arr, axis=0).tolist(), np.amax(arr, axis=1).tolist(), np.amax(arr.flat)]

def getSum(arr):
    return [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr.flat)]

def calculate(list):
    if len(list) != 9 or not all(type(x) is int for x in list):
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(list).reshape(3, 3)

    calculations = {
        'mean': getMean(arr),
        'variance': getVariance(arr),
        'standard deviation': getStdDev(arr),
        'max': getMax(arr),
        'min': getMin(arr),
        'sum': getSum(arr)
    }

    return calculations