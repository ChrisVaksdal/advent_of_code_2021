import numpy as np


def mostFrequentBin(l): # Returns most frequent bit in list of bits.
    return int(sum(l) >= (len(l) / 2))


def arrToNum(arr):  # Converts array of bits into decimal number.
    return int(("%d" * len(arr)) % tuple(arr), 2)


def getDiagnostic(arr, tarr, useMostCommon=True):           # Returns diagnostic number based on most or least common bit in each column.
    new_arr = arr
    for i in range(len(tarr)):

        if useMostCommon:
            crit = mostFrequentBin(tarr[i])                 # Get most common bit.
        else:
            crit = int(not bool(mostFrequentBin(tarr[i])))  # Get least common bit.

        new_arr = [el for el in new_arr if el[i] == crit]   # Filter out elements which dont satisfy bit criteria.

        if len(new_arr) == 1:
            return arrToNum(new_arr[0])

    print("Lol. Epic failure")
    exit()


def main():
    with open("input.txt", "r") as File:
        arr = np.array([[int(c) for c in line[:-1]] for line in File])  # [:-1] to avoid "\n".
        tarr = np.transpose(arr)

        oxygen = getDiagnostic(arr, tarr)
        co2 = getDiagnostic(arr, tarr, useMostCommon=False)

        print("Oxygen Generator Rating: %d" % oxygen)
        print("CO2 Scrubber Rating: %d" % co2)
        print("Life Support Rating: %d" % (oxygen * co2))


if __name__ == "__main__":
    main()
