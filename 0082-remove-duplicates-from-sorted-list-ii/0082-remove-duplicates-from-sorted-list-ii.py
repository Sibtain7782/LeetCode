class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # Duplicate found
            if curr.next and curr.val == curr.next.val:
                duplicate_val = curr.val

                # Skip all nodes with this value
                while curr and curr.val == duplicate_val:
                    curr = curr.next

                prev.next = curr

            else:
                prev = curr
                curr = curr.next

        return dummy.next