#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#
from typing import List
# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        if len(mat) == 1:
            return mat[0][0]
        for i, j in zip(range(len(mat)+1), range(len(mat)-1, -1, -1)):
            if i == j and len(mat) % 2 == 1:
                #print(f"({i}, {j})")
                sum = sum + mat[i][i]
            else:
                #print(f"({i}, {i}), ({j}, {i})")
                sum = sum + mat[i][i] + mat[j][i]
                
        return sum 
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.diagonalSum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]])
    print(output)
    
# [7,3,1,9]
# [3,4,6,9]
# [6,9,6,6]
# [9,5,8,5]