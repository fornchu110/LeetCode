<<<<<<< HEAD
#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# ���@��tree, return��tree�O�_����, ���ťN��̧Cheight�M�̰�height�ۮt���W�L1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive(bottom up), time: O(n) , space: O(n)
# space = O(n)�Ӧ�recursive��stack����, tree�̰��`�׳̴Nn
# �۷���Ǩ��X, �o�쵲�G��̷ӵ��G���P�_�M�w�nreturn����
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # height�P�ɺ�X�`�שM�P�_�O�_����, �����Ū��l�𰪫׷|�O-1
        def height(root: TreeNode) -> int:
            if not root:
                return True
            # ���T�{���k�l��O�_���ťH�Υ��k�l�𪺰���
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            # �u�n���k�l�𰪫׬ۮt�W�L1�Nreturn -1, ���k�䤤�O-1�N��w�g������, �ҥH�]�Oreturn -1
            if leftHeight==-1 or rightHeight==-1 or abs(leftHeight-rightHeight)>1:
                return -1
            # �J�M���Ũ��h�Fnode�o���I���״N�|�O���k�l����j��+1
            else:
                return max(leftHeight, rightHeight)+1
        # -1�N������, �ҥH�u�nreturn>=0�N�N����
        return height(root)>=0

# By recursive(top down), time: O(n^2) , space: O(n)
# �۷��e�Ǩ��X, �o�Ӥ�k��C�Ӥltree���|���Ҧ�node�T�{height
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         # ��­p���Uroot��tree�̤j����
#         def height(root: TreeNode) -> int:
#             if not root:
#                 return 0
#             # ��Utree���̤j���״N�O���k�l��̤j����+1��root, �]�N�O+1
#             return max(height(root.left), height(root.right))+1
#         if not root:
#             return True
#         # �u�n���k�l�𥭿ťB���k�l�𰪫׮t�b1�H���N�����tree����
#         return abs(height(root.left)-height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
# @lc code=end

=======
#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# ���@��tree, return��tree�O�_����, ���ťN��̧Cheight�M�̰�height�ۮt���W�L1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive(bottom up), time: O(n) , space: O(n)
# space = O(n)�Ӧ�recursive��stack����, tree�̰��`�׳̴Nn
# �۷���Ǩ��X, �o�쵲�G��̷ӵ��G���P�_�M�w�nreturn����
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # height�P�ɺ�X�`�שM�P�_�O�_����, �����Ū��l�𰪫׷|�O-1
        def height(root: TreeNode) -> int:
            if not root:
                return True
            # ���T�{���k�l��O�_���ťH�Υ��k�l�𪺰���
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            # �u�n���k�l�𰪫׬ۮt�W�L1�Nreturn -1, ���k�䤤�O-1�N��w�g������, �ҥH�]�Oreturn -1
            if leftHeight==-1 or rightHeight==-1 or abs(leftHeight-rightHeight)>1:
                return -1
            # �J�M���Ũ��h�Fnode�o���I���״N�|�O���k�l����j��+1
            else:
                return max(leftHeight, rightHeight)+1
        # -1�N������, �ҥH�u�nreturn>=0�N�N����
        return height(root)>=0

# By recursive(top down), time: O(n^2) , space: O(n)
# �۷��e�Ǩ��X, �o�Ӥ�k��C�Ӥltree���|���Ҧ�node�T�{height
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         # ��­p���Uroot��tree�̤j����
#         def height(root: TreeNode) -> int:
#             if not root:
#                 return 0
#             # ��Utree���̤j���״N�O���k�l��̤j����+1��root, �]�N�O+1
#             return max(height(root.left), height(root.right))+1
#         if not root:
#             return True
#         # �u�n���k�l�𥭿ťB���k�l�𰪫׮t�b1�H���N�����tree����
#         return abs(height(root.left)-height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
