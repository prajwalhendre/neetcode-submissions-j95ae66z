# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #prev starts off the actual list
        prev = None
        #curr starts at the head of the linked list
        curr = head

        while curr:
            #save the next node as a var so we can change what curr.next actually goes to
            nxt = curr.next
            #curr.next now points to previous
            curr.next = prev
            #move previous over for the next iteration
            prev = curr
            #move curr over for the next iteration
            curr = nxt
        #because curr is now out of range and not in the linked list, we return prev because it is the new head
        return prev

