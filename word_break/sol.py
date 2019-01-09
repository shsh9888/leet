class Solution:

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        '''
        words = {}
        stack = []
        for word in wordDict:
            words[word] =1
        if s in words:
            return True

        def check(start,end, string):
            if string[start:end] in words:
                if end is len(string):
                    return True
                ##keep track of the start to back track
                stack.append(start)

                if end < len(string):
                    return check(end, end+1, string)
                else:
                    return True
            else:
                if end < len(string):
                    return check(start,end+1,string)
                else:
                    if len(stack) !=0:
                        return check(stack.pop(), start+1,string)
                    else:
                        return False

        return check(0,1, s)


        '''
        ##Now we can solve this by dp.

        size = len(s)
        words = {}
        dp = [False] * (size+1)
        for word in wordDict:
            words[word] =1

        dp[0] = True

        for endIndex in range(1, size+1):
            for startIndex in range(endIndex):
                tmp_string = s[startIndex:endIndex]
                if dp[startIndex] and tmp_string in words:
                    dp[endIndex] =True

        return dp[-1]


Sol = Solution()

print(Sol.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
print(Sol.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
print(Sol.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))


print(Sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","b"]))