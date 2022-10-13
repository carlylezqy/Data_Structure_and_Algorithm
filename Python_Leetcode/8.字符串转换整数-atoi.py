#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        start_idx = 0 
        end_idx = 1
        key = False
        
        for i in s:
            if key:
                if i.isdigit():
                    end_idx += 1
                else:
                    break
            else:
                if i.isdigit():
                    key = True
                    end_idx = start_idx + 1
                else:
                    start_idx += 1
                
        if   s[start_idx-1] == '+':
            return int(s[start_idx:end_idx])
        elif s[start_idx-1] == '-':
            return -int(s[start_idx:end_idx])
        else:
            return int(s[start_idx:end_idx])
        
# @lc code=end
        
if __name__ == "__main__":
    solution = Solution()
    output = solution.myAtoi("words and 987")
    print(output)