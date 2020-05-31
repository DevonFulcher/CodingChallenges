# https://leetcode.com/problems/pascals-triangle/

'''
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def generate(numRows):
    if numRows == 0:
        return []
    answer = [[1]]
    previousRow = [1]
    if numRows == 1:
        return answer
    for i in range(numRows-1):
        currRow = [1]
        for j in range(len(previousRow)-1):
            currRow.append(previousRow[j] + previousRow[j+1])
        currRow.append(1)
        answer.append(currRow)
        previousRow = currRow
    return answer

