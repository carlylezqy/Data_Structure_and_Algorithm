#
# @lc app=leetcode.cn id=1313 lang=python3
#
# [1313] 解压缩编码列表
#
from typing import List
# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        opt = []
        for i in range(0, len(nums), 2):
            opt += [nums[i+1]] * nums[i]
        
        return opt

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.decompressRLElist([1,2,3,4])
    print(output)