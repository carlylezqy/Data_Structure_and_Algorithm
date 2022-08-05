#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        if s.find('IV') != -1:
            num += 4
            s = s.replace('IV', '')
        if s.find('IX') != -1:
            num += 9
            s = s.replace('IX', '')
        if s.find('XL') != -1:
            num += 40
            s = s.replace('XL', '')
        if s.find('XC') != -1:
            num += 90
            s = s.replace('XC', '')
        if s.find('CD') != -1:
            num += 400
            s = s.replace('CD', '')
        if s.find('CM') != -1:
            num += 900
            s = s.replace('CM', '')
        
        for i in s:
            num += dict[i]
            
        return num
            
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.romanToInt("MCMXCIV")
    print(output)