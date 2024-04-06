# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(ListNode):
    def mergeTwoLists(self, list1, list2):
        current = dummy = ListNode()
        while list1 and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next
    

        




        

        