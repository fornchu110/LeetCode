<<<<<<< HEAD
#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    def preorder(self, root:TreeNode, res):
        # �Dnode�N���ΰ����j�F
        if not root:
            return 
        #�e��:��->��->�k
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
        return

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #�^�Ǫ��O�}�C, �ҥH�@�}�l������l��
        res = []
        #��root�}�l���j��ʾ�node
        self.preorder(root, res)
        #���j��������, �^�ǫe�ǰl�ܵ��Gres
        return res

    
        
# @lc code=end

=======
#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    def preorder(self, root:TreeNode, res):
        # �Dnode�N���ΰ����j�F
        if not root:
            return 
        #�e��:��->��->�k
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
        return

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #�^�Ǫ��O�}�C, �ҥH�@�}�l������l��
        res = []
        #��root�}�l���j��ʾ�node
        self.preorder(root, res)
        #���j��������, �^�ǫe�ǰl�ܵ��Gres
        return res

    
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
