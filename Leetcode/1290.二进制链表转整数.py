#
# @lc app=leetcode.cn id=1290 lang=python3
#
# [1290] 二进制链表转整数
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ""
        while head.next != None:
            binary += str(head.val)
            head = head.next
        binary += str(head.val)
        return(int(binary,2))
        
# @lc code=end

