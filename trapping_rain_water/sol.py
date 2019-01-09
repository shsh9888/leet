class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ##basically the idea is that u need min and max at each point
        ## and keep deducting it by the minimum it will never be negative as current one could be min
        ## if its lesser than the min and max then this is filled
        size = len(height)
        if size is 0:
            return 0
        leftmax = [height[0]] * size
        rightmax = [height[size - 1]] * size

        ## calculating the left max at each point
        for i in range(1, size):
            leftmax[i] = max(leftmax[i - 1], height[i])
            if i != 1:
                rightmax[size - i] = max(height[size - i], rightmax[size - i + 1])

        ans = 0
        ab = []
        print(leftmax, rightmax)
        for index, h in enumerate(height):
            if index is 0 or index is size - 1:
                continue
            ab.append((min(leftmax[index], rightmax[index]), h))
            ans += min(leftmax[index], rightmax[index]) - h

        print(ab)
        return ans