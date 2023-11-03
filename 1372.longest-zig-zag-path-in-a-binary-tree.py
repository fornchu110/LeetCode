<<<<<<< HEAD
#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# ���@binary tree, return��tree���̪������path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS, time: O(n), space: O(1)
# �Q��DFS���j, �q�������_��s���צ�root
# �o�D�٥i�H��DP
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        # p_left�N��ۭ��parent�`�I��򨫤U��, True�N��O�������U��, False�N��O���k���U��
        def dfs(root: TreeNode, p_left: bool, long: int):
            nonlocal res
            # �פ����
            if not root:
                # �Dnode���|�W�[path�`��, ����return�Y�i
                return
            res = max(res, long)
            # �N��o���w�g���L����, �|���V�����X
            if p_left:
                # �p�G���L�����S�A����, �N��path���m, �]���S���
                dfs(root.left, True, 1)
                # ���L�����o����ܩ��k, ��path���צ��\+1
                dfs(root.right, False, long+1)
            # �N��o���w�g���L���k, �@�˷|���V�����X
            else:
                # ���L���k�o����ܩ���, ��path���צ��\+1
                dfs(root.left, True, long+1)
                # ���L���k��ܩ��k, �N��path���m
                dfs(root.right, False, 1)
        res = 0
        # �qroot�}�l, ���]�@�}�l�M�w�n������
        # ���󤣥Ω��k?���bdfs���Ҽ{�F, �����q�L��root��ڤW�S��V, �ӥBrecursive��Ӥ�V���|���X
        dfs(root, True, 0)
        return res
    
# @lc code=end

=======
#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# ���@binary tree, return��tree���̪������path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS, time: O(n), space: O(1)
# �Q��DFS���j, �q�������_��s���צ�root
# �o�D�٥i�H��DP
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        # p_left�N��ۭ��parent�`�I��򨫤U��, True�N��O�������U��, False�N��O���k���U��
        def dfs(root: TreeNode, p_left: bool, long: int):
            nonlocal res
            # �פ����
            if not root:
                # �Dnode���|�W�[path�`��, ����return�Y�i
                return
            res = max(res, long)
            # �N��o���w�g���L����, �|���V�����X
            if p_left:
                # �p�G���L�����S�A����, �N��path���m, �]���S���
                dfs(root.left, True, 1)
                # ���L�����o����ܩ��k, ��path���צ��\+1
                dfs(root.right, False, long+1)
            # �N��o���w�g���L���k, �@�˷|���V�����X
            else:
                # ���L���k�o����ܩ���, ��path���צ��\+1
                dfs(root.left, True, long+1)
                # ���L���k��ܩ��k, �N��path���m
                dfs(root.right, False, 1)
        res = 0
        # �qroot�}�l, ���]�@�}�l�M�w�n������
        # ���󤣥Ω��k?���bdfs���Ҽ{�F, �����q�L��root��ڤW�S��V, �ӥBrecursive��Ӥ�V���|���X
        dfs(root, True, 0)
        return res
    
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
