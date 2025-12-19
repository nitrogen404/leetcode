class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def toMinutes(time_str):
            hr, minute = map(int, time_str.split(":"))
            return hr * 60 + minute

        start1 = toMinutes(event1[0])
        end1 = toMinutes(event1[1])
        start2 = toMinutes(event2[0])
        end2 = toMinutes(event2[1])
        return not (end1 < start2 or end2 < start1) 