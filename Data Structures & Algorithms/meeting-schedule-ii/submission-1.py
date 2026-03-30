"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        s , e =0, 0
        max_rooms,  rooms =0, 0
        while s< len(intervals):
            if start[s]< end[e]:
                rooms +=1
                max_rooms = max(max_rooms, rooms)
                s+=1
            else:
                rooms-=1
                e+=1
        return max_rooms

        