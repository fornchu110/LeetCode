<<<<<<< HEAD
#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# �����tree, �n�D�X�֨�tree, �P�۹��m��node��value�n�ۥ[

# By recursive(DFS), time: O(min(m, n)), space: O(min(m, n)), m�Bn����tree��node��
# ��recursive�̷�root->���l->�k�l�����ǰ�preorder���X, ���tree�b�Ӧ�m�����Ůɤ~�|���X��
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # �p�G���@��tree�b����m�W�S��node, �N��o�Ӧ�m�|��t�@��tree��node.val
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        # merge�᪺tree node
        merged = TreeNode(t1.val+t2.val)
        # ���l�U�h���j
        merged.left = self.mergeTrees(t1.left, t2.left)
        # �k�l�U�h���j
        merged.right = self.mergeTrees(t1.right, t2.right)
        return merged

# By queue(BFS), time: O(min(m, n)), space: O(min(m, n)), m�Bn����tree��node��
# # �٨S��s
# class Solution:
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         if not t1:
#             return t2
#         if not t2:
#             return t1
        
#         merged = TreeNode(t1.val + t2.val)
#         queue = collections.deque([merged])
#         queue1 = collections.deque([t1])
#         queue2 = collections.deque([t2])

#         while queue1 and queue2:
#             node = queue.popleft()
#             node1 = queue1.popleft()
#             node2 = queue2.popleft()
#             left1, right1 = node1.left, node1.right
#             left2, right2 = node2.left, node2.right
#             if left1 or left2:
#                 if left1 and left2:
#                     left = TreeNode(left1.val + left2.val)
#                     node.left = left
#                     queue.append(left)
#                     queue1.append(left1)
#                     queue2.append(left2)
#                 elif left1:
#                     node.left = left1
#                 elif left2:
#                     node.left = left2
#             if right1 or right2:
#                 if right1 and right2:
#                     right = TreeNode(right1.val + right2.val)
#                     node.right = right
#                     queue.append(right)
#                     queue1.append(right1)
#                     queue2.append(right2)
#                 elif right1:
#                     node.right = right1
#                 elif right2:
#                     node.right = right2
        
#         return merged

# @lc code=end

=======
#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# �����tree, �n�D�X�֨�tree, �P�۹��m��node��value�n�ۥ[

# By recursive(DFS), time: O(min(m, n)), space: O(min(m, n)), m�Bn����tree��node��
# ��recursive�̷�root->���l->�k�l�����ǰ�preorder���X, ���tree�b�Ӧ�m�����Ůɤ~�|���X��
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # �p�G���@��tree�b����m�W�S��node, �N��o�Ӧ�m�|��t�@��tree��node.val
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        # merge�᪺tree node
        merged = TreeNode(t1.val+t2.val)
        # ���l�U�h���j
        merged.left = self.mergeTrees(t1.left, t2.left)
        # �k�l�U�h���j
        merged.right = self.mergeTrees(t1.right, t2.right)
        return merged

# By queue(BFS), time: O(min(m, n)), space: O(min(m, n)), m�Bn����tree��node��
# # �٨S��s
# class Solution:
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         if not t1:
#             return t2
#         if not t2:
#             return t1
        
#         merged = TreeNode(t1.val + t2.val)
#         queue = collections.deque([merged])
#         queue1 = collections.deque([t1])
#         queue2 = collections.deque([t2])

#         while queue1 and queue2:
#             node = queue.popleft()
#             node1 = queue1.popleft()
#             node2 = queue2.popleft()
#             left1, right1 = node1.left, node1.right
#             left2, right2 = node2.left, node2.right
#             if left1 or left2:
#                 if left1 and left2:
#                     left = TreeNode(left1.val + left2.val)
#                     node.left = left
#                     queue.append(left)
#                     queue1.append(left1)
#                     queue2.append(left2)
#                 elif left1:
#                     node.left = left1
#                 elif left2:
#                     node.left = left2
#             if right1 or right2:
#                 if right1 and right2:
#                     right = TreeNode(right1.val + right2.val)
#                     node.right = right
#                     queue.append(right)
#                     queue1.append(right1)
#                     queue2.append(right2)
#                 elif right1:
#                     node.right = right1
#                 elif right2:
#                     node.right = right2
        
#         return merged

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
