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
        while list2.next is not None:
            while list1.next is not None:
                if list1.val >= list2.val:
                    pointer = list1.next
                    list1.next = list2
                    list2 = list2.next
                    list1.next.next = pointer
                else:
                    pass
            list1 = list1.next
            
        return list1
# @lc code=end

if __name__ == "__main__":
    solutioin = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    output = solutioin.mergeTwoLists(list1, list2)
    print(output)