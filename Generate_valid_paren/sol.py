class Solution(object):
    validLists =[]
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.allParenthesis(n)
        return self.validLists

    def allParenthesis(self, n, open=0, close=0, parenString=""):
        if len(parenString) == 2*n:
            self.validLists.append(parenString)
            return

            # print("open,close",open,close)
            # if self.isValidSet(parenString):
            ## there is no need to do this as well, It will always give u the valid set
            #     self.validLists.append(parenString)
            #     return
            # return
        if open < n:
            self.allParenthesis(n,open+1, close, parenString+"(")
        # parenString = parenString[:len(parenString)-1]
        if close <open: ##
            self.allParenthesis(n, open, close+1,parenString+")")
        # parenString = parenString[:len(parenString)-1]

    ## no use of this though
    def isValidSet(self, parenString):
        size = len(parenString)
        if size is 0 or size%2 != 0 or parenString[0]==")":
            return False

        stack =[]
        for x in parenString:
            if x is "(":
                stack.append(x)
            if x is ")":
                if len(stack) == 0 or stack.pop() is not "(":
                    return False

        if len(stack) == 0:
            return True
        else: return False


sol = Solution()
print(sol.generateParenthesis(3))