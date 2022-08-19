#
# @lc app=leetcode.cn id=1450 lang=python3
#
# [1450] 在既定时间做作业的学生人数
#

# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = [1 for s, e in zip(startTime, endTime) if queryTime in range(s, e+1)]
        return sum(count)
# @lc code=end

