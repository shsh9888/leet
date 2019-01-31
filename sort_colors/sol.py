class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        index =0
        count =0
        zeroIndex =0
        twoIndex = size-1
        while (index <= twoIndex): ## and the trick is here moving till the 2 index as insorted ones
            count +=1
            if nums[index] is 2:
                nums[index],nums[twoIndex] = nums[twoIndex],nums[index]
                twoIndex = twoIndex -1
                index =index -1 ## trick is here
            elif nums[index] is 0:
                nums[index],nums[zeroIndex] = nums[zeroIndex],nums[index]
                zeroIndex = zeroIndex + 1
            # if nums[index] is 1:
            index += 1




        print(count,nums)


sol = Solution()
print(sol.sortColors([2,0,2,0,1,0,0,0,1,1,0]))