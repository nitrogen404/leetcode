class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        i, count, end, farthest = 0, 0, 0, 0
        while end < time:
            while i < len(clips) and clips[i][0] <= end:
                farthest = max(farthest, clips[i][1])
                i += 1
            if farthest == end:
                return -1
            end = farthest
            count += 1
        return count
        
