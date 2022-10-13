#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#
import itertools
from typing import List
# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_num = 0
        for i in range(0, len(arr)+1):
            for j in range(0, len(arr)+1, 1):
                if (j - i) % 2 == 1 and j - i >= 0 and j - i <= len(arr):
                    #print(i, j)
                    sum_num += sum(arr[i:j])
        return sum_num

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.sumOddLengthSubarrays([1,4,2,5,3])
    print(output)
