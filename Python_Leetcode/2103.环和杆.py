#
# @lc app=leetcode.cn id=2103 lang=python3
#
# [2103] 环和杆
#

# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        if(len(rings) < 6):
            return 0
        count = [1 for i in range(10) if f"R{i}" in rings and f"G{i}" in rings and f"B{i}" in rings]
        return sum(count)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.countPoints("B0R0G0R9R0B0G0")
    print(output)