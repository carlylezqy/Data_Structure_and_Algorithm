#
# @lc app=leetcode.cn id=2325 lang=python3
#
# [2325] 解密消息
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dedup = iter({}.fromkeys(key.replace(' ','')).keys())
        dictionary = {next(dedup):chr(i) for i in range(97,123)} #dict(zip(key.replace(' ',''), []))
        dictionary[' '] = ' '
        return ''.join([dictionary[i] for i in message])
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
    print(output)
    