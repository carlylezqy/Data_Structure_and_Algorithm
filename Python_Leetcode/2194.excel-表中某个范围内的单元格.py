#
# @lc app=leetcode.cn id=2194 lang=python3
#
# [2194] Excel 表中某个范围内的单元格
#
from typing import List
# @lc code=start
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        opt = []
        a, b = s.split(':')
        for i in range(ord(a[0]), ord(b[0])+1):
            for j in range(int(a[1]), int(b[1])+1):
                opt.append(f"{chr(i)}{j}")
        
        return opt
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    output = solution.cellsInRange("K1:L2")
    print(output)
    