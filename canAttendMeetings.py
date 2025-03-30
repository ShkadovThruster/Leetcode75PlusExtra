"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        i=0
        end=len(intervals)
        while (i<end-1):
            if intervals[i+1].start<intervals[i].end:
                return False
            i+=1
        return True
