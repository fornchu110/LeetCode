<<<<<<< HEAD
#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#By recursive
class Solution:
    def postorder(self, root:TreeNode, res):
        #���j�פ����, �Y�Dnode���λ��j
        if not root:
            return
        #���:��->�k->��
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)
        return

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #��l�ƭn�^�Ǫ��}�Cres
        res = list()
        #�qroot�}�l��Ҧ�node����ǰl��
        self.postorder(root, res)
        #��Ҧ�node�����j����, �^�ǵ��G
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#By recursive
class Solution:
    def postorder(self, root:TreeNode, res):
        #���j�פ����, �Y�Dnode���λ��j
        if not root:
            return
        #���:��->�k->��
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)
        return

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #��l�ƭn�^�Ǫ��}�Cres
        res = list()
        #�qroot�}�l��Ҧ�node����ǰl��
        self.postorder(root, res)
        #��Ҧ�node�����j����, �^�ǵ��G
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
