'''
56. Merge Intervals
Medium
Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''

class Solution(object):

    def merge_two(self, one, two):
        smin = min (one[0], two[0])
        emax = max (one[1], two[1])
        return [smin, emax]
    
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals is None or len(intervals) == 0:
            return intervals
        
        # loop through interval and do merge
        result = []
        interval_dict = {} # number to interval mapping
        
        n = len(intervals)
        for i in range(n):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]

            found_intervals = {}
            for j in range (start, end + 1):
                print(f"NUMBER {j}")
                if j in interval_dict:
                    the_interval = interval_dict[j]
                    _start = the_interval[0]
                    if _start not in found_intervals:
                        found_intervals[_start] = the_interval

            for k in found_intervals:
                intervaltwo = found_intervals[k]
                print(f"before merge: {interval} {intervaltwo}")
                interval = self.merge_two(interval, intervaltwo)
                print(f"after merge: {interval}")

            start = interval[0]
            end = interval[1]
            for m in range(start, end +1):
                interval_dict[m] = interval

        start_set = set()
        for key in interval_dict:
            _interval = interval_dict[key]
            if _interval[0] not in start_set:
                start_set.add(_interval[0])
                result.append(_interval)

        return result

result = Solution().merge([[2,3],[4,6],[5,7],[3,4]])
for r in result:
    print (r)