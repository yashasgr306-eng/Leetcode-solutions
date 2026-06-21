class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

       
            total = x + y + carry
            carry = total // 10

            current.next = ListNode(total % 10)

            current = current.next
            
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
           
