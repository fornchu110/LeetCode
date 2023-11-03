#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# ���@��BST, �n�Dreturn BST����k�p����

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS(recursive), time: O(n), space: O(n)
# ������BST���S�ʪ������X�@�M����U��node��val, �Ƨǫ�return��k�p
# ���M�g�����Ҽ{�S�ʦӤ��αƧ�, ������h���Ψ��Xn��node�����k, �H��A�Q
class Solution:
    # �Ĥ@�ӬOnonlocal���@�k, �NDFS�g���l�禡
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # �b�~���ŧires
        res = []
        def DFS(node):
            # �̭��ŧires�Ononlocal, �Ϩ��X�L�{��N���X�쪺node.val�[�Jres
            nonlocal res
            # �פ����, �Dnode�Nreturn
            if node is None:
                return 
            # �Ҽ{BST�S�ʪ���, �i�H�o�{BST��inorder���X���G�N��n�O���ǼƦC
            # recursive���l->��node�n������->recursive�k�l
            DFS(node.left)
            # �Onode�N�Nval�[�Jres, �åB�~�򩹥��l�M�k�l���X
            res.append(node.val)
            DFS(node.right)
        # �qroot�}�lrecursive
        DFS(root)
        # �Nres��1�p���N�O��0��, �ҥHreturn res[k-1]
        return res[k-1]
    
    # �NDFS�g�b�~��, �]�N�O�@��class���t�@�Ө禡���g�k 
    # �]��res�O�b�O���禡�w�q, �ҥH�n�z�L�Ѽƶǻ�
    # def DFS(self, node, res):
    #     if node is None:
    #         return 
    #     self.DFS(node.left, res)
    #     res.append(node.val)
    #     self.DFS(node.right, res)

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     res = []
    #     self.DFS(root, res)
    #     return res[k-1]
        
# @lc code=end

