'''

'''

'''
We are given information about the connections in the network and the security level for each computer. 
Security level is the time (in minutes) that is required for the virus to capture a machine. 
Capture time is not related to the number of infected computers attacking the machine. 
Infection start from the 0th computer (which is already infected). 
Connections in the network are undirected. Security levels are not equal to zero (except infected).

Information about a network is represented as a matrix NxN size, 
where N is a number of computers. If i th computer connected with j th computer, 
then matrix[i][j] == matrix[j][i] == 1, else 0. Security levels are placed in the 
main matrix diagonal, so matrix[i][i] is the security level for the i th computer.
'''

def capture(matrix):
    future = [(0, 0)]
    infected = []
    while len(future) > 0:
        future.sort()
        t, computer = future[0]
        if computer not in infected:
            infected.append(computer)
        if len(infected)==len(matrix[computer]):
            return t
        del future[0]
        for victim, is_victim in enumerate(matrix[computer]):
            if computer is victim:
                continue
            if is_victim == 1 and victim not in infected:
                future.append((t+matrix[victim][victim], victim))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"