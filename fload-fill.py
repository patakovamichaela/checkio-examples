from typing import Tuple, List

def printPicture(vector):
    for px in test:
        print(px)
    print(f'-----------------------------')

def checkBoundraries(vector, coord : Tuple [int, int]) -> bool:
    return (coord[0] > (len(vector) -1) or coord[0] < 0) or (coord[1] > (len(vector[0]) -1) or coord[1] < 0)

def fillPolygon(vector,visited, x,y) -> None:
    neighbours = [[x-1, y],[x+1, y],[x,y+1],[x,y-1]]
    for coord in neighbours:
        if checkBoundraries(vector, coord) == True:
            continue
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

