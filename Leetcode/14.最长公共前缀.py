#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_char = ''
        break_flag = False
        
        for i in range(min([len(str) for str in strs])):
            for str in strs:
                if str[i] != strs[0][i]:
                    break_flag = True
                                            
            if break_flag:
                return common_char
            else:
                common_char += strs[0][i]
            
        return common_char
                
            
# @lc code=end

if __name__ == '__main__':
    solutioin = Solution()
    output = solutioin.longestCommonPrefix(strs=["flower","flow","flight"])
    print(output)
