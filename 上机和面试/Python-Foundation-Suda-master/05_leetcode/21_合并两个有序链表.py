"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = []
        ptr = self
        while ptr:
            res.append(ptr.val)
            ptr = ptr.next
        return res

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 32ms 98.35%
        l3 = ListNode()
        p3 = l3
        while l1 and l2:
            if l1.val > l2.val:
                p3.next = l2
                l2 = l2.next
            else:
                p3.next = l1
                l1 = l1.next
            p3 = p3.next
        if l1 is not None:
            p3.next = l1
        elif l2 is not None:
            p3.next = l2
        return l3.next
        
    def mergeTwoLists2(self, l1, l2):
        # 递归且避免 长链逐个添加
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2




if __name__ == "__main__":
    pass