#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack, output = [], ""
        for i in s:
            if i == ')':
                stack.pop()
            
            if len(stack) != 0:
                output += i

            if i == '(':
                stack.append(i)
                
        return output
                    
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    output = solution.removeOuterParentheses("(()())(())")
    print(output)
