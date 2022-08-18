#
# @lc app=leetcode.cn id=1913 lang=python3
#
# [1913] 两个数对之间的最大乘积差
#
from typing import List
# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return((nums[-2] * nums[-1]) - (nums[0] * nums[1])) 

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.maxProductDifference([4,2,5,9,7,4,8])
    print(output)