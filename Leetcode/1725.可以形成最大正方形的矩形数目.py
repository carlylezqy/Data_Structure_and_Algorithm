#
# @lc app=leetcode.cn id=1725 lang=python3
#
# [1725] 可以形成最大正方形的矩形数目
#
from typing import List
import numpy as np
# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        opt = []
        for i in rectangles:
            opt.append(min(i))
        return opt.count(max(opt))
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]])
    print(output)