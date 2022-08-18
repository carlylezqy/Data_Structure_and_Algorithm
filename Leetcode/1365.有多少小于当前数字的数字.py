#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#
from typing import List
# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        opt = [0] * 101
        
        for i in nums:
            opt[i] += 1
        
        return [sum(opt[:i]) for i in nums]
            
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.smallerNumbersThanCurrent([8,1,2,2,3])
    print(output)

