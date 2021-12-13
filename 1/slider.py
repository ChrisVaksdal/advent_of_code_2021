with open("input.txt", "r") as File:
    lines = [int(line) for line in File]
    n = 3
    windows = [lines[i:i+n] for i in range(len(lines) + 1 - n)]
    cnt = 0
    prev = windows[0]
    for window in windows[1:]:
        if sum(window) > sum(prev):
            cnt += 1
        prev = window
    print("Number of increases: %d" % cnt)