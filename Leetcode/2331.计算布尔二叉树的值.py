#
# @lc app=leetcode.cn id=2331 lang=python3
#
# [2331] 计算布尔二叉树的值
#
from turtle import right
from typing import Optional
from xmlrpc.client import boolean
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.

class Solution:    
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return bool(root.val)
        
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        return bool(left or right) if root.val == 2 else bool(left and right)

# @lc code=end

if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
    solution = Solution()
    output = solution.evaluateTree(root)
    print(output)
    
