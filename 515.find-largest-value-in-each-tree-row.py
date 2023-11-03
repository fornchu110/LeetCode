#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ���@Tree��root, retun�@��list���e�Otree���U��level��node.val�̤j��

# By BFS, time: O(n), space:o(n)
# �N�O��BFS���覡���X, �`�N�Clevel�n�O���ثe�̤jnode.val�Y�i
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        # �إ�deque��list�B�@�ٮ�
        queue = collections.deque()
        queue.append(root)
        # ��queue�٦������N�N��tree�٨S���X��
        while(len(queue)):
            # �n����̤j��, �ҥH����l�Ƥ@�ӭt�L���p
            maxtmp = float("-inf")
            # �C������o��⪺���״N�O��level��node��
            n = len(queue)
            # ��᭱n��node, �]�N�O��level��node
            for i in range(n):
                # �@�@pop�X�ӬݭȬO�_�̤j�H�Φ�child�N�[�Jqueue
                tmpnode = queue.popleft()
                maxtmp = max(maxtmp, tmpnode.val)
                if tmpnode.left is not None:
                    queue.append(tmpnode.left)
                if tmpnode.right is not None:
                    queue.append(tmpnode.right)
            # ��level���Ҧ�node���ݹL�ȥB�L�̪�child���Q�[�Jqueue
            # res���[�J��level�̤j��
            res.append(maxtmp)
        return res


# @lc code=end

