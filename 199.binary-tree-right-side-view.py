#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# ���@��tree, �n�Dreturn tree�C�@level�̥k�䪺����

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS, time: O(n), space: O(n)
# ��BFS���X, �C�������@��level�N�̧��ݤ����[�Jres�Y�i
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        res = []
        queue = collections.deque([root])
        # �C�B�z�@��level�|�P�_�@��while
        while queue:
            # ��tmp�x�s�C�@level��node.val
            tmp = []
            # n�N�O��level�Ҧ���node�ƶq
            n = len(queue)
            # �קK�B�z�줣�Plevel��node
            for i in range(n):
                node = queue.popleft()
                # �O�o�nappend���Onode.val���Onode
                tmp.append(node.val)
                # ���ONone�~�n�[�Jqueue, �]���o�ˤ~��value�Mchild
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # queue�������~�|����j��, �ҥH���ξ��tmp�������ųy����out of range
            # ��tmp.pop()�|��C
            res.append(tmp[n-1])
        return res

# @lc code=end

