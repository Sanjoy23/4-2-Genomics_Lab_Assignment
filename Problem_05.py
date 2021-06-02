import numpy as np


def updateMatrix(distanceMatrix, i, minValTrack):
    newDisMatrix = np.zeros((i,i))
    position = findMinValueposition(distanceMatrix)
    minValTrack[i][0] = position[0]
    minValTrack[i][1] = position[1]

    x = 0
    y = 1
    for j in range(len(distanceMatrix)):
        if j == position[1]:
            continue
        y = x + 1
        for k in  range(j+1,len(distanceMatrix)):
            if k == position[1]:
                continue

            if j == position[0]:
                temp = min(distanceMatrix[position[0]][k], distanceMatrix[position[1]][k])
                newDisMatrix[x][y] = newDisMatrix[y][x] = temp
            else:
                newDisMatrix[x][y] = newDisMatrix[y][x] = distanceMatrix[j][k]
            y = y+1
        newDisMatrix[x][x] = 0
        x = x+1

    return newDisMatrix

def printMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end =" ")
        print("\n")
    print("\n")
    return

def build_DistanceMatrix(feature):
    length = len(feature)
    distanceMatrix = np.zeros((length,length))

    for i in range(length):
        for j in range(length):
            if i == j:
                distanceMatrix[i][j] = 0
            else:
                distanceMatrix[i][j] = distanceMatrix[j][i] = abs(feature[i] - feature[j])


    return distanceMatrix

def findMinValueposition(matrix):
    miniVal = 100
    position = np.zeros(2)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if miniVal > matrix[i][j]:
                miniVal = matrix[i][j]
                position[0] = i
                position[1] = j

    return position

def main():
    feature = [1,2,5,6,8]
    Gene = ['a', 'b', 'c', 'd', 'e']
    minValTrack = [[0 for i in range(2)] for j in range(len(Gene)+1)]

    distanceMatrix = build_DistanceMatrix(feature)
    cnt = 1
    for i in range(len(feature), 1, -1):
        print("Number of step "+str(cnt))
        printMatrix(distanceMatrix)
        distanceMatrix = updateMatrix(distanceMatrix, i,  minValTrack)
        cnt = cnt + 1
    print(print("Number of step "+str(cnt)))
    printMatrix(distanceMatrix)

main()