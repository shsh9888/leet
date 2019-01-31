class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.topmost =-1

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.topmost is -1:
            self.stack.append((x,x))
        else:
            self.stack.append((x,min(x, self.stack[self.topmost][1])))

        self.topmost +=1

    def pop(self):
        """
        :rtype: void
        """
        if self.topmost > -1:
            popped = self.stack[-1]
            self.stack = self.stack[:(len(self.stack))-1]
            self.topmost -= 1
            return popped
    def top(self):
        """
        :rtype: int
        """
        if self.topmost >= -1:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.topmost > -1:
            return self.stack[-1][1]

