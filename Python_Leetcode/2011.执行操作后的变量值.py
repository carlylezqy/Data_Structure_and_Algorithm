#
# @lc app=leetcode.cn id=2011 lang=python3
#
# [2011] 执行操作后的变量值
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0
        for i in operations:
            if '+' in i:
                sum += 1
            else:
                sum -= 1
        return sum
    
# @lc code=end

