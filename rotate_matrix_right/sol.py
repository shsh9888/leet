class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        n = len(matrix)
        start = 0
        end = n

        loop = n // 2

        while loop > 0:
            j = 0
            for i in range(start, end - 1):
                # print(matrix[start][i], matrix[i][end-1],matrix[end-1][end-1-i],matrix[end-1-i][start] , "-->",matrix[end-1-i][start],matrix[start][i],matrix[i][end-         1],matrix[end-1][end-1-i])

                matrix[start][i], matrix[i][end - 1], matrix[end - 1][end - 1 - j], matrix[end - 1 - j][start] = \
                matrix[end - 1 - j][start], matrix[start][i], matrix[i][end - 1], matrix[end - 1][end - 1 - j]
                j += 1
            loop -= 1
            start += 1
            end -= 1

        print("Answer:",matrix)
        # return matrix


sol = Solution()
sol.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])

sol.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])