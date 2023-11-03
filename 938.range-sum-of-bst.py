#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive dfs, time: O(n), space: O(n ) 
#�@�˻��j, �n�ݪ��O�C�`�I��value�N�n
#�`���u���j��DFS
#BST���l��p�k�l��j
class Solution:
 def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        #���j�פ����
        if not root:
            return 0
        #��node��high�٤j, �k�l�@�w�]��high�j���Χ�, �N�n����p��node��, �ҥH�䥪�l
        if root.val>high:
            return self.rangeSumBST(root.left, low, high)
        #��node��low�٤p, ���l�@�w�]��low�p���Χ�, �N�n����j��node��, �ҥH��k�l
        if root.val<low:
            return self.rangeSumBST(root.right, low, high)
        #���A�X���I, �]�N�O����[low, high]�K�N��[�J���פ�, �B�ѩ�O�����ҥH���l�k�l���i��O����
        return root.val+self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

# By bfs, time: O(n), space: O(n)
# class Solution:
#     def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
#         total = 0
#         q = collections.deque([root])
#         while q:
#             node = q.popleft()
#             if not node:
#                 continue
#             if node.val > high:
#                 q.append(node.left)
#             elif node.val < low:
#                 q.append(node.right)
#             else:
#                 total += node.val
#                 q.append(node.left)
#                 q.append(node.right)

#         return total

# @lc code=end

