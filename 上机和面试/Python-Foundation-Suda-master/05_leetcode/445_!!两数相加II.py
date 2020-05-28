"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        ptr = self
        while ptr:
            print(ptr.val, end='->')
            ptr = ptr.next 
        else:
            print('None')

    @staticmethod
    def generate(link):
        priv,head = None,None
        for num in link:
            L = ListNode(num)
            if priv:
                priv.next = L
            else:
                head = L
            priv = L
        return head
            

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        # 108ms
        L1, L2, L3 = [], [], []
        # 取出两条链的数
        while l1 != None:
            L1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            L2.append(l2.val)
            l2 = l2.next
        # 计算两链重合部分的和
        flag = 0
        for i in range(1, min(len(L1), len(L2))+1):
            temp = L1[-i] + L2[-i] + flag
            flag = 1 if temp >= 10 else 0
            L3.append(temp % 10)
        target = L1 if len(L1) > len(L2) else L2
        # 长链剩余部分与
        index = len(target) -i -1
        while flag:
            if index <0:
                target.insert(0, 1)
                flag = 0
            else:
                flag, target[index] = divmod(target[index] + flag, 10)
                # L3.insert(0, target[index])
                index -= 1
        # 重合部分没有进位
        # L3.extend(reversed(target[:len(target) - i]))
        L3.extend(reversed(target[:len(target) - i]))
        # 生成链表
        priv,head = None,None
        for num in reversed(L3):
            L = ListNode(num)
            if priv:
                priv.next = L
            else:
                head = L
            priv = L
        return head

    def addTwoNumbers2(self, l1: ListNode, l2:ListNode):
        # 84ms
        # 堆栈法！！
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans

if __name__ == "__main__":
    # L1 = ListNode.generate([1])
    # L2 = ListNode.generate([9, 9])
    L1 = ListNode.generate([7,2,4,3])
    L2 = ListNode.generate([5,6,4])
    L1.show()
    L2.show()
    s = Solution()
    L3 = s.addTwoNumbers(L1, L2)
    L3.show()