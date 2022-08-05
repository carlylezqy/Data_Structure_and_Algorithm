#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
# @lc code=end

if __name__ == "__main__":
    solutioin = Solution()
    output = solutioin.mergeTwoLists(list1=[1,2,4], list2=[1,3,4])
    print(output)