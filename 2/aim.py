with open("input.txt", "r") as File:
    pos = [0, 0, 0]
    for line in File:
        verb, l = line.split()

        if verb == "forward":
            pos[0] += int(l)
            pos[1] += pos[2] * int(l)
        elif verb == "up":
            pos[2] -= int(l)
        elif verb == "down":
            pos[2] += int(l)
        
    print("Final position: (%d, %d)" % (pos[0], pos[1]))
    print("Sum: %d" % (pos[0] * pos[1]))