#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, product = 0, 1
        for i in str(n):
            sum += int(i)
            product *= int(i)
        
        return product-sum
            
# @lc code=end

