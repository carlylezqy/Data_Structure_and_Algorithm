#
# @lc app=leetcode.cn id=1920 lang=python3
#
# [1920] 基于排列构建数组
#
from typing import List

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        opt = []
        for i, _ in enumerate(nums):
            opt.append(nums[nums[i]])
        return opt
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.buildArray([0,2,1,5,3,4])
    print(output)