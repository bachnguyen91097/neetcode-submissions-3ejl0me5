class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
#         0,0 -> 0,1
#         0,1 -> 1,1
#         1,1 -> 1,0
#         1,0 -> 0,0


#  3 x 3
#         0,0 -> 0,2 #1 -> 3 
#         0,1 -> 1,2 #2 -> 6
#         0,2 -> 2,2 #3 -> 9
#         1,2 -> 2,1 #6 -> 8
#         2,2 -> 2,0 #9 -> 7
#         2,1 -> 1,0 #8 -> 4
#         2,0 -> 0,0 #7 -> 1
#         1,0 -> 0,1 #4 -> 2
# top = 0 , bottom = 2, left = 0, right = 2
#         1,1 -> 1,1 #5 -> 5

# [x,y] = [y, n - 1 - x]
        n = len(matrix)
        top, left = 0, 0
        bottom, right = n - 1, n - 1
        while top <= bottom and left <= right:
            if top == bottom == left == right:
                return
            for i in range(left, right):
                temp = matrix[top][i]
                matrix[top][i] = matrix[n - 1 - i][left]
                matrix[n - 1 - i][left] = matrix[bottom][n - 1 - i]
                matrix[bottom][n-1-i] = matrix[i][right]
                matrix[i][right] = temp
            top += 1
            right -= 1
            bottom -= 1
            left += 1
        

