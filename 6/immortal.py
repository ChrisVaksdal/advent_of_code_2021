import numpy as np

INPUT_FILE_PATH = "input.txt"
NUM_DAYS_PREGNANT = 7               # How many days before a lanternfish spawns a child.
NUM_DAYS_INFERTILE = 2              # How many days before a lanternfish can reproduce.
NUM_DAYS_TOTAL = 256                # How many days the observation will go on for.

def cycleDay(lanterns):
    lanterns -= 1
    inLabor = np.where(lanterns == -1)
    if inLabor[0].size > 0:
        lanterns[inLabor] = NUM_DAYS_PREGNANT - 1
        babyLanterns = np.array([NUM_DAYS_PREGNANT + NUM_DAYS_INFERTILE - 1] * len(inLabor[0]))
        lanterns = np.append(lanterns, babyLanterns)
    return lanterns

def main():
    with open(INPUT_FILE_PATH, "r") as File:
        lanterns = np.array([int(fish) for fish in File.readline().split(",")])
    for _ in range(NUM_DAYS_TOTAL):
        lanterns = cycleDay(lanterns)
    print("After %d days, there will be %d lanternfish in total." % (NUM_DAYS_TOTAL, len(lanterns)))



if __name__ == "__main__":
    main()
