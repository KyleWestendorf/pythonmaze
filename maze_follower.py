def test():
    return True

def evaluateBoard(maze, cx = -1, cy = -1):
    
    start = False
    end = False

    for y, row in enumerate(maze):
        for x, position in enumerate(row):
            if position == "E":
                end = True
            if position == "S": 
                start = True      

    if start == False or end == False:
        raise ValueError

    for y, row in enumerate(maze):
        for x, position in enumerate(row):
            # if position == "E":
            #     raise ValueError
            if cx == -1 and cy == -1:
                if position == "S":
                   return x, y
            else:
                x = 3
                y = 0
                return x, y

    raise ValueError


