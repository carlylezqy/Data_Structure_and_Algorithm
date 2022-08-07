#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#
from typing import List
# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums):
                if i < j and v1 == v2:
                    count += 1
        return count
                    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.numIdenticalPairs([1,2,3,1,1,3])
    print(output)
