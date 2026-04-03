"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)


        for interval in range(len(intervals)):
            if interval == 0:
                continue
            else:
                if intervals[interval].start < intervals[interval -1].end:
                    return False
        return True