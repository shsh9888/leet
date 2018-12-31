# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        '''
        ## this would work if the intervals were list but here it is separate python objecct
        if len(intervals) is 0:
            return []
        out = []
        intervals = sorted(intervals, key=lambda x:x[0])
        for interval in intervals:
            if not out or out[-1][1] < interval[0]:
                out.append(interval)
            else:
                out[-1][1] = max(out[-1][1], interval[1])
        return out
        '''

        ## as it is an interval object
        intervals.sort(key=lambda x:x.start)
        if len(intervals) is 0:
            return []
        out = []
        for interval in intervals:
            if not out or out[-1].end < interval.start:
                out.append(interval)
            else:
                out[-1].end = max(out[-1].end, interval.start)
        return out


sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
