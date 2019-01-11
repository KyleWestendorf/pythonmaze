def test():
    return True

def evaluateBoard(maze):
    for i, row in enumerate(maze):
        for j, position in enumerate(row):
            if position == "E":
                raise ValueError
            if position == "S":
                raise ValueError

    raise ValueError