class ListNode(object):
    def __init__(self, x):
        self.val= x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow,fast,h,cur = head,head,head,head
        while fast is not None and fast.next is not None:
            slow,fast = slow.next, fast.next.next

            if slow is fast: ## there is a cylce, here slow will end up in between a loop
                while h != slow: ## so
                    h,slow = h.next,h.next

                ##if we have to remove the loop
                # while cur.next != h:
                #     cur = cur.next
                # cur.next = None


        return None ## no cycle loop ended