import numpy as np

def mostFrequentBin(l): # Returns most frequent bit in list of bits.
    return int(sum(l) > (len(l) / 2))

with open("input.txt", "r") as File:
    arr = np.transpose([[int(c) for c in line[:-1]] for line in File])              # Get transposed array of bits.
    gamma = int(("%d" * len(arr)) % tuple([mostFrequentBin(l) for l in arr]), 2)    # Each bit of gamma is most common bit in each column of arr.
    epsilon = int("1" * len(arr), 2) ^ gamma                                        # Epsilon is simply bitwise inverse of gamma.
    print("Product: %d" % (gamma * epsilon))
    