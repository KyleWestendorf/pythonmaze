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
            elif position == " ":
                print(cy, y, x, cx)
                if y == cy and x - 1 == cx:
                    return x, y
                            
    raise ValueError

def leaveBreadCrumb(maze, cy, cx):
    maze = maze[0][0:cx] + '*' + maze[0][cx+1:]
    return [maze]
   
