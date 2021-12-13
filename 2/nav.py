with open("input.txt") as File:
    pos = [0, 0]
    for line in File:
        verb, l = line.split()

        if verb == "forward":
            pos[0] += int(l)
        elif verb == "up":
            pos[1] = max(0, pos[1] - int(l))
        elif verb == "down":
            pos[1] += int(l)
    
    print("Final position: (%d, %d)" % (pos[0], pos[1]))
    print("Sum: %d" % (pos[0] * pos[1]))