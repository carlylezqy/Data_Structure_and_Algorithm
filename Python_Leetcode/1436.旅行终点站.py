#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#
from typing import List
# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict_paths = {i[0]:i[1] for i in paths}
        dict = {}
        for key in [j for i in paths for j in i]:
            dict[key] = dict.get(key, 0) + 1
        
        idx = [i for i in dict.keys() if dict[i] == 1 and (i not in dict_paths.keys())][0]
        return idx
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    output = solution.destCity([["B","C"],["D","B"],["C","A"]])
    print(output)
