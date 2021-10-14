'''
You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)

'''
from typing import List, Tuple
import math

Coords = List[Tuple[int, int]]

def sideLength(a: tuple, b: tuple):
    
    length = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return length
    
def angle(a, b, c : int):
    return(math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c))))

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    sidesABC = list(map(sideLength, (coords_1[0], coords_1[1], coords_1[2]), (coords_1[1], coords_1[2], coords_1[0])))
    anglesABC = list()
    sidesDEF = list(map(sideLength, (coords_2[0], coords_2[1], coords_2[2]), (coords_2[1], coords_2[2], coords_2[0])))
    anglesDEF = list()
    for s in range(0,3):
        anglesABC.append(angle(sidesABC[s%3], sidesABC[(s+1)%3], sidesABC[(s+2)%3]))
        anglesDEF.append(angle(sidesDEF[s%3], sidesDEF[(s+1)%3], sidesDEF[(s+2)%3]))
    anglesABC.sort()
    anglesDEF.sort()
    cnt=0
    for a in range(0,3):
        if (anglesABC[a] == anglesDEF[a]):
            cnt += 1
        if (cnt == 2):
            return True
    
    return False


if __name__ == '__main__':
    print("Example:")
    #print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'