"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 错误 仅仅递归判断 左 < x < 右
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.isValidBST(root.right) and self.isValidBST(root.left)

    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历递增 非递归  左入栈  出栈后访问 并入栈右侧
        temp = root
        queue, last = [], None
        while temp:
            queue.append(temp)
            temp = temp.left
        while queue:
            temp = queue.pop()
            if last is not None:
                if temp.val <= last:
                    return False
            last = temp.val
            if temp.right:
                # 存在右节点 则将右节点左链入栈
                temp = temp.right
                while temp:
                    queue.append(temp)
                    temp = temp.left
        return True
            

