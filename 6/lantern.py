INPUT_FILE_PATH = "input.txt"
NUM_DAYS_PREGNANT = 7               # How many days before a lanternfish spawns a child.
NUM_DAYS_INFERTILE = 2              # How many days before a lanternfish can reproduce.
NUM_DAYS_TOTAL = 80                 # How many days the observation will go on for.

def cycleDay(lanterns):
    for i, fish in enumerate(lanterns):
        if fish:
            lanterns[i] -= 1
        else:
            lanterns[i] = NUM_DAYS_PREGNANT - 1
            lanterns.append(NUM_DAYS_PREGNANT + NUM_DAYS_INFERTILE)
    return lanterns

def main():
    with open(INPUT_FILE_PATH, "r") as File:
        lanterns = [int(fish) for fish in File.readline().split(",")]
    for _ in range(NUM_DAYS_TOTAL):
        lanterns = cycleDay(lanterns)
    print("After %d days, there will be %d lanternfish in total." % (NUM_DAYS_TOTAL, len(lanterns)))



if __name__ == "__main__":
    main()
