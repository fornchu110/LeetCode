<<<<<<< HEAD
#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# ���@��tree, return��tree�������I�̪���path����

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS, time: O(n), space: O(height)
# space = O(height)�O�]recursive�һݭn��stack�Ŷ�, �]�N�Orecursive�`��, �btree�N�O��
# path���׬O�g�L��node��-1
# �̪����|�|��root����subtree�̪�+�ksubtree�̪��Ҳզ�
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 1
        # ��X��tree�̪�(�]�N�O�̲`)�����|�M�ktree�̪����|���M
        def depth(node):
            nonlocal res
            # �פ����, ��Dnode��return
            if node is None:
                return 0
            # �䥪�ltree�`��
            L = depth(node.left)
            # ��k�ltree�`��
            R = depth(node.right)
            # �N��̬ۥ[, ��+�Wroot�����ҥH+1
            # res�Ononlocal��, ���j�L�{����return res�]�b���_��s
            res = max(res, L+R+1)
            # ���j�L�{�nreturn���O��node���k�ltree�̤j�`��
            return max(L, R)+1
        # �Hroot���X�o�I
        depth(root)
        return res-1
        
# @lc code=end

=======
#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# ���@��tree, return��tree�������I�̪���path����

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS, time: O(n), space: O(height)
# space = O(height)�O�]recursive�һݭn��stack�Ŷ�, �]�N�Orecursive�`��, �btree�N�O��
# path���׬O�g�L��node��-1
# �̪����|�|��root����subtree�̪�+�ksubtree�̪��Ҳզ�
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 1
        # ��X��tree�̪�(�]�N�O�̲`)�����|�M�ktree�̪����|���M
        def depth(node):
            nonlocal res
            # �פ����, ��Dnode��return
            if node is None:
                return 0
            # �䥪�ltree�`��
            L = depth(node.left)
            # ��k�ltree�`��
            R = depth(node.right)
            # �N��̬ۥ[, ��+�Wroot�����ҥH+1
            # res�Ononlocal��, ���j�L�{����return res�]�b���_��s
            res = max(res, L+R+1)
            # ���j�L�{�nreturn���O��node���k�ltree�̤j�`��
            return max(L, R)+1
        # �Hroot���X�o�I
        depth(root)
        return res-1
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
