"""

给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        pass

    def areSame(self, T1, T2):
        if T1 is None and T2 is None:
            return True
        elif not (T1 and T2):
            return False
        elif T1.val != T2.val:
            return False
        else:
            return self.areSame(T1.left, T2.right) and self.areSame(T1.right, T2.right)
        

if __name__ == "__main__":
    pass