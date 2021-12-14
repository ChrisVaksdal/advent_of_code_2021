INPUT_FILE_PATH = "input.txt"

def main():

    with open(INPUT_FILE_PATH) as File:
        crabPositions = [int(pos) for pos in File.readline().split(",")]

    numPossiblePositions = max(crabPositions) + 1
    lowestPosition = min(crabPositions)

    # Count number of occurrences for each position and store in list:
    posOccurrences = [0] * numPossiblePositions
    for i in range(numPossiblePositions):
        posOccurrences[i] = crabPositions.count(i)

    # For each possible target position, calculate cost based on how many crabs are in each location:
    lowestFuelcost = -1
    bestPos = -1
    for target in range(numPossiblePositions):
        fuel = 0
        for pos, num in enumerate(posOccurrences):
            distance = abs(target - pos + lowestPosition)   # Distance from current position to target.
            cost = sum(range(distance + 1))                 # Increasing cost per move means cost to target is equal to sum of range.
            fuel += cost * num                              # Num crabs at pos * cost per crab = total cost.

        if fuel < lowestFuelcost or lowestFuelcost == -1:
            lowestFuelcost = fuel
            bestPos = target

    print("The best position for the crabs is %d. Getting all of them there will cost %d fuel" % (bestPos, lowestFuelcost))


if __name__ == "__main__":
    main()
