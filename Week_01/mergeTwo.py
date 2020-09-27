class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(-1)
        pre=dummy
        while l1 and l2:
            if l1.val<=l2.val:
                pre.next=l1
            else:
                pre.next=l2
            pre=pre.next
        pre.next=l1 if l1 else l2
        return dummy.next
