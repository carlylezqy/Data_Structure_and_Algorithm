#
# @lc app=leetcode.cn id=1720 lang=python3
#
# [1720] 解码异或后的数组
#
from typing import List
# @lc code=start
class Solution:
    def XOR(self, i1, i2):
        #return int((not i1 and i2) and (i1 and not i2))
        return i1 ^ i2
    
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [0] * (len(encoded) + 1); arr[0] = first
        for i in range(len(encoded)):
            arr[i + 1] = self.XOR(arr[i], encoded[i])
        return arr
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    output = solution.decode([1, 2, 3], 1)
    print(output)

# 关于异或运算的几条基本定理

# 异或满足结合律，    (a^b)^c = a^(b^c)
# 异或满足交换律，        a^b = b^a
# 任意数与自身异或得0，    a^a = 0
# 任意数异或0的到自身，    a^0 = a
# 推导过程如下，E[i]表示encoded[i]，A[i]表示arr[i]：

# 已知 E[i] = A[i] ^ A[i+1]
# 等式两边同时右异或A[i]，等号仍然成立，E[i] ^ A[i] = A[i] ^ A[i+1] ^ A[i]
# 由定理1，E[i] ^ A[i] = A[i] ^ (A[i + 1] ^ A[i])
# 由定理2，E[i] ^ A[i] = A[i] ^ (A[i] ^ A[i+1])
# 由定理1，E[i] ^ A[i] = (A[i] ^ A[i]) ^ A[i+1]
# 由定理3，E[i] ^ A[i] = 0 ^ A[i+1]
# 由定理4，E[i] ^ A[i] = A[i+1]