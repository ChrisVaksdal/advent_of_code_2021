import numpy as np
import sys

with open("input.txt", "r") as File:
    lineFrom, lineTo = list(), list()
    for line in File:
        lf, _, lt = line.split()
        lineFrom.append(tuple(int(l) for l in lf.split(",")))
        lineTo.append(tuple(int(l) for l in lt.split(",")))

    lft = np.transpose(lineFrom)
    ltt = np.transpose(lineTo)

    width = max(np.max(lft[0]), np.max(ltt[0]))
    height = max(np.max(lft[1]), np.max(ltt[1]))
    
    board = np.zeros((width, height))

    for i in range(len(lineFrom)):
        fx, fy = lineFrom[i]
        tx, ty = lineTo[i]

        if fx == tx:    # Vertical lines:
            l = abs(ty - fy) + 1                                # Calculate length of line
            vec = np.concatenate(                               # Create vector containing line of 1s in correct place.
                (
                    np.zeros(min(fy, ty) - 1), 
                    np.ones(l),
                    np.zeros(height - l - min(fy, ty) + 1)
                ), axis=0
            )
            add = np.zeros((width - 1, height))                 # Create matrix with same shape as board minus vec.
            add = np.insert(add, fx, vec, axis=0)               # Insert vec into add, making it same size as board.
            board += add                                        # Add new line of 1s to board.

        elif fy == ty:  # Horizontal lines (works same way as vertical ones, just with the axes switched):
            l = abs(tx - fx)  + 1
            vec = np.concatenate(
                (
                    np.zeros(min(fx, tx) - 1),
                    np.ones(l),
                    np.zeros(width - l - min(fx, tx) + 1)
                ), axis=0
            )
            add = np.zeros((width, height - 1))
            add = np.insert(add, fy, vec, axis=1)
            board += add
        
    numOverlappingLines = len(board[np.where(board > 0)])
    print("Number of points where two or more lines overlap\p: %d" % numOverlappingLines)
    print(np.max(board))