# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = {}
        c = head
        prev = None
        
        while c:
            if c.val not in d:
                d[c.val] = 1
                prev = c
            else:
                prev.next = c.next
            c = c.next
        
        return head