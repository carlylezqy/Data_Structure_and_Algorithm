#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#
import math
from typing import List
# @lc code=start
class Solution:
    def Dist(self, P1, P2):
        opt = [abs(p2-p1) for (p1,p2) in zip(P1,P2)]
        return max(opt)
    
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        for i, _ in enumerate(points[:-1]):
            distance += self.Dist(points[i+1], points[i])
        return distance
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
    print(output)