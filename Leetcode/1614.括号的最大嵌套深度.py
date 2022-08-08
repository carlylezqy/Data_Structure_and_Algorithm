#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_nesting_depth = 0
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
                max_nesting_depth = max(max_nesting_depth, len(stack)+1)
                
        return max_nesting_depth
        
# @lc code=end

if __name__ == "__main__":
    soultion = Solution()
    output = soultion.maxDepth("(()(())())")
    print(output)