#
# @lc app=leetcode.cn id=1389 lang=python3
#
# [1389] 按既定顺序创建目标数组
#
from typing import List
# @lc code=start
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        value = []
        for i, n in zip(index, nums):
            value.insert(i, n)
        
        return value

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1])
    print(output)