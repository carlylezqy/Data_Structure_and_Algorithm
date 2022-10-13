#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.removeElement(nums=[3,2,2,3], val=3)
    print(output)