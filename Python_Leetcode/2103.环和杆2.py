#
# @lc app=leetcode.cn id=2103 lang=python3
#
# [2103] 环和杆
#

# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        dict = {i:[] for i in range(10)}
        exclusion = []
        count = 0
        for i in range(0, len(rings), 2):
            color, idx = rings[i:i+2]
            dict[int(idx)].append(color)
            if set(dict[int(idx)]) == {'R', 'G', 'B'} and idx not in exclusion:
                count += 1
                exclusion.append(idx)
        return count
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.countPoints("B0R0G0R9R0B0G0")
    print(output)