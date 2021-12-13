def getBoards(lines):   # Retrieve boards as 2D-lists from lines of input file.
    boards = []

    i = -1
    for line in lines:
        if line == "":
            boards.append([])
            i += 1
            continue
        boards[i].append([int(num) for num in line.split()])
    return boards


def applyDraw(board, draw): # Replace all instances of draw in board with None.
    return [
        [
            number if number != draw else None for number in row
        ]
        for row in board
    ]


def checkRow(row):  # Returns whether a given row is fully drawn.
    return all(el is None for el in row)


def checkColumn(board, i):  # Returns whether a board has a fully drawn column at given index.
    nums = [row[i] for row in board]
    return all(el is None for el in nums)


def checkBoard(board):  # Returns whether a board contains a fully drawn row or column.
    for row in board:
        if checkRow(row):
            return True
    for i in range(len(board[0])):
        if checkColumn(board, i):
            return True
    return False


def scoreBoard(board, lastDraw):    # Calculate score of given board.
    s = 0
    for row in board:
        s += sum([num for num in row if num])
    return s * lastDraw


def main():
    with open("input.txt", "r") as File:
        draws = [int(draw) for draw in File.readline().split(",")]
        lines = [line[:-1] for line in File]
        boards = getBoards(lines)

        winners = []

        for draw in draws:
            for i, board in enumerate(boards):
                if i in [windex[0] for windex in winners]:  # Skip boards that have already won.
                    continue
                boards[i] = applyDraw(board, draw)  # Overwrite board with checked board
                if checkBoard(boards[i]):
                    winners.append((i, draw))
                    
        print("Score of last board to win: %d" % scoreBoard(boards[winners[-1][0]], winners[-1][1]))
                    

if __name__ == "__main__":
    main()