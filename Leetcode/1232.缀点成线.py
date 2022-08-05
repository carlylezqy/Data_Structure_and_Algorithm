#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        
        for index in coordinates[1:]:
            x, y = index[0], index[1]
            if(x2 == x1 or y2 == y1):
                if((x2 == x1 and x != x1) or (y2 == y1 and y != y1)):
                    return False
            else:
                if ((x - x1)/(x2 - x1) != (y - y1)/(y2 - y1)):
                    return False

        return True
# @lc code=end

