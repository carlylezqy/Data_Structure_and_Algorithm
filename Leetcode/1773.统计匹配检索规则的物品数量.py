#
# @lc app=leetcode.cn id=1773 lang=python3
#
# [1773] 统计匹配检索规则的物品数量
#
from typing import List
# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        dict = {"type": 0, "color": 1, "name": 2}
        for i in items:
            if i[dict[ruleKey]] == ruleValue:
                count += 1
        
        return count

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone")
    print(output)
