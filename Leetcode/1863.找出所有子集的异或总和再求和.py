#
# @lc app=leetcode.cn id=1863 lang=python3
#
# [1863] 找出所有子集的异或总和再求和
#
import itertools
from typing import List
# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum = 0
        for a in range(len(nums)):
            for i in itertools.combinations(nums, a+1):
                XOR_SUM = 0
                for set in i:
                    XOR_SUM ^= set
                sum += XOR_SUM
        
        return sum
        
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.subsetXORSum([0])
    print(output)