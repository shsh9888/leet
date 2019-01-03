class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        '''
        ## this will work but the problem here is that it will take all cases 
        ## time will be exceeded
        self.count =0
        def uni(m_,n_):
            if m_ is m and n_ is n:
                self.count +=1
                return

            if m_< m:
                uni(m_+1,n_)
            if n_ < n:
                uni(m_,n_+1)
        uni(1,1)
        return self.count
        '''
        ##Now what if I can use dp, Use the same matrix and see if how mant steps at each point
        ## with the base condition that first row and column would be zeros
        matrix = [[1]*m]*n
        if m is 1 or n is 1:
            return m*n

        ## fill the first row and colum with 1s

        # for i in range(m):
        #     matrix[0][i] =1
        # for i in range(m):
        #     matrix[i][0] =1

        for i in range(1,n):
            for j in range(1,m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        # print(matrix)
        return matrix[n-1][m-1]










Sol = Solution()
print(Sol.uniquePaths(7,3))
