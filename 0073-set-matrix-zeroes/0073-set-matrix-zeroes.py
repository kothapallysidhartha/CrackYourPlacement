class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        xaxis = set()
        yaxis = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    xaxis.add(i)
                    yaxis.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in xaxis or j in yaxis:
                    matrix[i][j] = 0
