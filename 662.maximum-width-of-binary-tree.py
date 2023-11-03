<<<<<<< HEAD
#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# ���@��tree, return tree���̼s���s�׬O�h��
# �O��e�פ�����C�h�`�I�ƶq, �ӬO�Ӽh�̥k��M�̥���node��index�t��

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS, time: O(n), space: O(n)
# ��array���x�s, ����b��binary tree��parent�Mchild��index���Y
# ��X�C�h���e�׫�D�̤j��, �e�ץѨC�h�̤j�s��node��index��h�̤p�s��node��index+1�o�X
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # ��l��array, ��Jroot���ɬO�Ĥ@�h, �̼e�O1�Broot��index = 1
        res = 1
        # �C�h�|��J�Ӽh��node
        queue = collections.deque()
        # �O��append�@���@�Ӥ���
        queue.append([root, 1])
        while queue:
            # ��tmp�s���U�h�ƪ�node
            tmp = collections.deque()
            for node, index in queue:
                # ���lindex�|�Oparent index*2
                if node.left:
                    tmp.append([node.left, index*2])
                # �k�lindex�|�Oparent index*2+1
                if node.right:
                    tmp.append([node.right, index*2+1])
            # �̤j�s��index-�̤p�s��index, �p�G��res�٤j�N��sres
            # �W�@�h�˼ƲĤ@��node(�̥k��)��index-�W�@�h��0��node(�̥���)��index+1
            res = max(res, queue[-1][1]-queue[0][1]+1)
            # ��sarr���U�@�h��, �Ytmp���ťN��o�h�Snode, �]�N�O�w�g�S���h��ݤF, ���X�j��
            queue = tmp
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# ���@��tree, return tree���̼s���s�׬O�h��
# �O��e�פ�����C�h�`�I�ƶq, �ӬO�Ӽh�̥k��M�̥���node��index�t��

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS, time: O(n), space: O(n)
# ��array���x�s, ����b��binary tree��parent�Mchild��index���Y
# ��X�C�h���e�׫�D�̤j��, �e�ץѨC�h�̤j�s��node��index��h�̤p�s��node��index+1�o�X
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # ��l��array, ��Jroot���ɬO�Ĥ@�h, �̼e�O1�Broot��index = 1
        res = 1
        # �C�h�|��J�Ӽh��node
        queue = collections.deque()
        # �O��append�@���@�Ӥ���
        queue.append([root, 1])
        while queue:
            # ��tmp�s���U�h�ƪ�node
            tmp = collections.deque()
            for node, index in queue:
                # ���lindex�|�Oparent index*2
                if node.left:
                    tmp.append([node.left, index*2])
                # �k�lindex�|�Oparent index*2+1
                if node.right:
                    tmp.append([node.right, index*2+1])
            # �̤j�s��index-�̤p�s��index, �p�G��res�٤j�N��sres
            # �W�@�h�˼ƲĤ@��node(�̥k��)��index-�W�@�h��0��node(�̥���)��index+1
            res = max(res, queue[-1][1]-queue[0][1]+1)
            # ��sarr���U�@�h��, �Ytmp���ťN��o�h�Snode, �]�N�O�w�g�S���h��ݤF, ���X�j��
            queue = tmp
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
