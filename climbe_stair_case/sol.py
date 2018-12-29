class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        this will work but isnt dynamic programming much cooler
        self.total =0

        def climb(sum):
            if sum == n:

                self.total +=1
                return
            if sum > n:
                return

            climb(sum+1)
            climb(sum+2)
            ##climb(sum+1) + climb(sum+2) better hn?
            
        climb(0)
        return self.total
        '''
        ##climb(sum+1) + climb(sum+2) better hn?
        ### once u write that u should know that its dynamic
        dp ={}
        dp[1] =1
        dp[2] =2
        for i in range(3, n+1):
            dp[i] =dp[i-1] +dp[i-2]
        return dp[n]

sol = Solution()

print(sol.climbStairs(4))