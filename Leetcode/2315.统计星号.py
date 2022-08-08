#
# @lc app=leetcode.cn id=2315 lang=python3
#
# [2315] 统计星号
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        for i, v in enumerate(s.split("|")):
            if i % 2 == 0:
                count += v.count("*")
        return count
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.countAsterisks("yo|uar|e**|b|e***au|tifu|l")
    print(output)