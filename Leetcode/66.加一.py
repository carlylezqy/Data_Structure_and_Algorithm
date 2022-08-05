#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from typing import List
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        #for i, v in enumerate(:
        i = 0
        digits = digits[::-1]
        while i < len(digits):
            if digits[i] == 10 and i != len(digits) - 1:
                digits[i] = 0
                digits[i+1] += 1
                
            if digits[i] == 10 and i == len(digits) - 1:
                digits[-1] = 0
                digits.insert(len(digits), 1)
                break
            
            i += 1
        
        return digits[::-1]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.plusOne(digits=[9, 9, 9])
    print(output)
    