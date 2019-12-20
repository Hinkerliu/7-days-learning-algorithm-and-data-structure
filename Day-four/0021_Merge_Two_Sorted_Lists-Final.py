# Final modified from 0021_Merge_Two_Sorted_Lists.py 
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dummy head
        pos = dummyHead = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next
            pos = pos.next
        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        pos.next = l1 if l1 else l2

        return dummyHead.next