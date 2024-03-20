import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def generator(a):
    # random number to normal distribution 
    normal_distributed_random = np.random.normal(0, 1, a)  
    # apply the fuction
    normalized_random = sigmoid(normal_distributed_random)  
    # cut out number over
    normalized_random = np.clip(normalized_random, 0, 1)  
    return normalized_random