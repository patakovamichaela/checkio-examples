
test = [[0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,1,1,1,1,1,0],
        [0,0,0,0,0,1,0,0,0,0,1,0],
        [0,0,0,0,0,1,0,0,1,1,1,0],
        [0,0,0,0,0,1,0,0,1,0,0,0],
        [0,0,0,0,0,1,0,0,1,0,0,0],
        [0,0,0,0,0,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]]

def printPicture(test):
    for i in test:
        print(i)
    print(f'-----------------------------')

def checkBoundraries(vector, x,y):
    maxHeight=len(vector)
    maxWidth=len(vector[0])
    if ((x < 0) or (x > maxWidth - 1)) or ((y < 0) or (y > maxHeight -1)):
        return False
    return True

def fillPolygon(vector,visited, x,y):
    neighbours = [[x-1, y],[x+1, y],[x,y+1],[x,y-1]]
    for coord in neighbours:
        value = vector[coord[0]][coord[1]]
        if value == 0:
            vector[coord[0]][coord[1]] = 1
            visited.append(coord)
        elif coord in visited:
            continue
        elif value == 1:
            continue
            visited.append(coord)
        fillPolygon(vector, visited, coord[0], coord[1])


printPicture(test)
visited = list()
fillPolygon(test,visited,5,6)
printPicture(test)

def assertWrapper(vector, x,y):
    visited = list()
    fillPolygon(vector,visited,x,y)
    return vector


assert assertWrapper([[0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,1,1,0,0,0],
        [0,0,0,1,0,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,0,1,0,0,0],
        [0,0,0,1,1,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]],5,5) == [[0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,1,1,1,1,1,1,0,0,0],
                                        [0,0,0,1,1,1,1,1,1,0,0,0],
                                        [0,0,0,1,1,1,1,1,1,0,0,0],
                                        [0,0,0,1,1,1,1,1,1,0,0,0],
                                        [0,0,0,1,1,1,1,1,1,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0,0,0,0,0]]