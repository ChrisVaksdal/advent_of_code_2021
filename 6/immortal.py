INPUT_FILE_PATH = "input.txt"
NUM_DAYS_PREGNANT = 7               # How many days before a lanternfish spawns a child.
NUM_DAYS_INFERTILE = 2              # How many days before a lanternfish can reproduce.
NUM_DAYS_TOTAL = 256                # How many days the observation will go on for.

NUM_STATES = NUM_DAYS_PREGNANT + NUM_DAYS_INFERTILE


def main():
    with open(INPUT_FILE_PATH, "r") as File:
        lanterns = [int(fish) for fish in File.readline().split(",")]

    # Create a list containing how many lanternfish are in each state of gestation.
    timerStates = [0] * NUM_STATES
    for i in range(NUM_STATES):
        timerStates[i] = lanterns.count(i)
    
    # Every day, move each element in the list one to the left. Add number in 0th position to both 7th and 9th positions.
    for _ in range(NUM_DAYS_TOTAL):
        newTimerStates = [timerStates[i + 1] for i in range(NUM_STATES - 1)]
        newTimerStates[NUM_DAYS_PREGNANT - 1] += timerStates[0]
        newTimerStates.append(timerStates[0])
        timerStates = newTimerStates

    print("After %d days, there will be %d lanternfish in total." % (NUM_DAYS_TOTAL, sum(timerStates)))


if __name__ == "__main__":
    main()
