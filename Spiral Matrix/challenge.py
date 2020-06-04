# https://leetcode.com/problems/spiral-matrix/

'''
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
answer = [1,2,3,6,9,]
'''

def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    matrixSize = len(matrix) * len(matrix[0])
    rightBound = len(matrix[0])
    bottomBound = len(matrix)
    leftBound = 0
    topBound = 0
    currX, currY = 0, 0
    answer = [matrix[0][0]]
    while True:
        while currX < rightBound-1:
            answer.append(matrix[currX][currY])
            currX += 1
        rightBound -= 1
        if len(answer) != matrixSize:
            break

        while currY < bottomBound-1:
            answer.append(matrix[currX][currY])
            currY += 1
        bottomBound -= 1
        if len(answer) != matrixSize:
            break

        while currX >= leftBound-1:
            answer.append(matrix[currX][currY])
            currX -= 1
        leftBound += 1
        if len(answer) != matrixSize:
            break

        while currY >= topBound-1:
            answer.append(matrix[currX][currY])
            currY -= 1
        topBound += 1
        if len(answer) != matrixSize:
            break
    return answer
        