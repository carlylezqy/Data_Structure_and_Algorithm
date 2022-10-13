#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#
from typing import List
# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        R = 0; L = 0 
        for i in s:
            if i == 'R':
                R += 1
            else:
                L += 1

            if R == L:
                R = 0
                L = 0
                count += 1
                
        return count
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.balancedStringSplit("LLLLRRRR")
    print(output)