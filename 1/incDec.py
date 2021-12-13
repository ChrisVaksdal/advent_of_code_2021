with open("input.txt") as File:
    numIncreased = 0
    prev = int(File.readline())
    for line in File:
        if int(line) > prev:
            numIncreased += 1
        prev = int(line)
    print("Number of increases: %d" % numIncreased)

cnt = sum(1 for line in open("input.txt", "r"))
print("Total number: %d" % cnt)