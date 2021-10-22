from typing import Tuple, List

coordinates = Tuple [int, int]
array2d = List [List [int]]

def printPicture(vector : array2d) -> None:
    for px in vector:
        print(px)
    print(f'-----------------------------')

def checkBoundraries(vector : array2d, coord : coordinates) -> bool:
    return (coord[0] > (len(vector) -1) or coord[0] < 0) or (coord[1] > (len(vector[0]) -1) or coord[1] < 0)

def fillPolygon(vector: array2d, visited : List[int], coord: coordinates) -> None:
    neighbours = [[coord[0]-1, coord[1]],[coord[0]+1,coord[1]],[coord[0],coord[1]+1],[coord[0],coord[1]-1]]
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
        fillPolygon(vector, visited, coord)

def assertWrapper(vector: array2d, coord : coordinates) -> array2d:
    if checkBoundraries(vector, coord) == True:
        return None
    visited = list()
    fillPolygon(vector,visited,coord)
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
        [0,0,0,0,0,0,0,0,0,0,0,0]],[5,5]) == [[0,0,0,0,0,0,0,0,0,0,0,0],
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
        [0,0,0,0,0,0,0,0,0,0,0,0]],[30,5]) == None

assert assertWrapper([[0,0,0],
                      [0,0,0],
                      [0,0,0]], [2,1]) == [[1,1,1],
                                          [1,1,1],
                                          [1,1,1]]