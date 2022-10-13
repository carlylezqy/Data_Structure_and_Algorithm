#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#
from typing import List
# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..'}        
        opt = []
        for word in words:
            opt.append(''.join([morse[char] for char in word]))
        
        return len(set(opt))
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"])
    print(output)