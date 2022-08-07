#
# @lc app=leetcode.cn id=2160 lang=python3
#
# [2160] 拆分数位后四位数字的最小和
#
from typing import List
# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = []
        for i in str(num):
            num_list.append(int(i))
        num_list.sort()
        return 10 * (num_list[0] + num_list[1]) + num_list[2] + num_list[3]
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    output = solution.minimumSum(4009)
    print(output)