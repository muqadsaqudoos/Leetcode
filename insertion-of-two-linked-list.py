# Definition for singly-linked list.
#class ListNode:
 #   def __init__(self, x):
  #      self.val = x
   #     self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Definition for singly-linked list.
            def get_length(x):
                        len = 0
                        while x:
                            len +=1
                            x = x.next
                        return len
            temp1 = headA
            temp2 = headB

            len_A = get_length(temp1)
            len_B = get_length(temp2)

            if len_A >len_B:
                while len_A != len_B:
                    temp1 = temp1.next
                    len_A -=1
            else:
                while len_A != len_B:
                    temp2 = temp2.next
                    len_B -= 1
                            
            while temp1 != temp2:
                    temp1 = temp1.next
                    temp2 = temp2.next
                
            return temp1


        