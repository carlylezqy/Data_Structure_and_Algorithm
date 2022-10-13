#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#

# @lc code=start
class Solution:
    def __init__(self):
        super().__init__()
        self.count = 0
        
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return self.count
        elif num % 2 == 0:
            num /= 2
            self.count += 1
        elif num % 2 == 1:
            num -= 1
            self.count += 1

        
        return self.numberOfSteps(num)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.numberOfSteps(14)
    print(output)