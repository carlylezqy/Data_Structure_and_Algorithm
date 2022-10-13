#
# @lc app=leetcode.cn id=2037 lang=python3
#
# [2037] 使每位学生都有座位的最少移动次数
#
#
from typing import List
# @lc code=start
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        total_count = 0
        seats.sort(); students.sort()
        for i in range(len(students)):
            total_count += abs(seats[i] - students[i])
        
        return(total_count)
                
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.minMovesToSeat(seats = [4,1,5,9], students = [1,3,2,6])
    print(output)