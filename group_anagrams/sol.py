class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        '''
        ## this will work but can I do without sorting
        ## with keys as the sorted strings
        dict ={}
        for str in strs:
            sortedStr = "".join(sorted(str))
            if sortedStr in dict:
                dict[sortedStr].append(str)
            else:
                dict[sortedStr] =[str]

        ans = []
        for strL in dict.values():
            ans.append(strL)

        return ans
        ## I dont know why I did that I could have just returned dict.values() !! lol
        '''

        ##Well one of the things that is same in the anagrams is that number of counts of each char
        ## but problem is that how can I make that a key and store it
        ## well python is amazing.. tuple can be a key
        ## ord function can be used to get the ascii value in python
        dict = {}
        for str in strs:
            counts =[0]*26
            ##create a countarry for each string
            for s in str:
                counts[ord(s)-ord('a')] +=1
            #tupple it and store it as a key
            tup = tuple(counts)
            if tup in dict:
                dict[tup].append(str)
            else:
                dict[tup] =[str]
        return list(dict.values())


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

