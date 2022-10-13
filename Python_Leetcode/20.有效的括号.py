#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if i == ')' :
                    if len(stack) > 0 and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif i == ']':
                    if len(stack) > 0 and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif i == '}':
                    if len(stack) > 0 and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        if len(stack) != 0:
            return False
        else:
            return True
# @lc code=end
if __name__ == "__main__":
    solutioin = Solution()
    output = solutioin.isValid(s="}")
    print(output)