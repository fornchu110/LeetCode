<<<<<<< HEAD
#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n^2), space: O(n), n�Olen(nums)
# ��array, �C����array���̤j�ȷ�node, �A�ӥ��l���̤j�ȩҦbindex���barr, �k�l���̤j�ȩҦbindex�k�barr
# �]�C�����n���X��M�̤j��, �ҥH��nums�ƧǹL���N�O���a���p
# �n�Hindex�@���Ѽƶǻ��M�פ����
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # left�Bright�Bmax�O�s��nums�Ϊ�index
        def build(left, right):
            # �פ����
            # index�@�w�O�q�p��j, �����}�C�d��index�ܦ��j��p, �N�N����
            if left>right:
                return None
            # max�����ثe�o�q�̤j�ȩҦb��index
            max = left
            for i in range(left+1, right+1):
                if nums[i]>nums[max]:
                    max = i
            # �N�̤j�ȫئ�node
            node = TreeNode(val = nums[max])
            # ���l�|�O���䨺�q�̤j��node
            node.left = build(left, max-1)
            # �k�l�|�O�k�䨺�ݳ̤j��node
            node.right = build(max+1, right)
            return node
        # �]�ѼƬOindex, array��index�q0�}�l, len(nums)-1����
        return build(0, len(nums)-1)

# By stack, time: O(n), space: O(n)
# �γ��stack�ӫ�tree, ���ӭ쥻�n�D���C����̤jvalue
# ���stack�O�@�Ӥ�����ƥu�|���W�λ���ƧǪ�stack
# �ӬO�ھڥثe���X�쪺val��W�Ӥj�٤p�@�۹������P�ʧ@, push��pop
# tree�����D�ئn�����n�Q�Q���γ��stack��
# �b��ƶq���h���ɭԦ]�����@������Ƶ��c�]�n��ɶ�, �ĪG�|��W���t
# �٨S����
# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
#         n = len(nums)
#         stk = list()
#         left, right = [-1]*n, [-1]*n
#         tree = [None]*n

#         for i in range(n):
#             tree[i] = TreeNode(nums[i])
#             while stk and nums[i] > nums[stk[-1]]:
#                 right[stk[-1]] = i
#                 stk.pop()
#             if stk:
#                 left[i] = stk[-1]
#             stk.append(i)
        
#         root = None
#         for i in range(n):
#             if left[i] == right[i] == -1:
#                 root = tree[i]
#             elif right[i] == -1 or (left[i] != -1 and nums[left[i]] < nums[right[i]]):
#                 tree[left[i]].right = tree[i]
#             else:
#                 tree[right[i]].left = tree[i]
        
#         return root

# @lc code=end

=======
#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n^2), space: O(n), n�Olen(nums)
# ��array, �C����array���̤j�ȷ�node, �A�ӥ��l���̤j�ȩҦbindex���barr, �k�l���̤j�ȩҦbindex�k�barr
# �]�C�����n���X��M�̤j��, �ҥH��nums�ƧǹL���N�O���a���p
# �n�Hindex�@���Ѽƶǻ��M�פ����
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # left�Bright�Bmax�O�s��nums�Ϊ�index
        def build(left, right):
            # �פ����
            # index�@�w�O�q�p��j, �����}�C�d��index�ܦ��j��p, �N�N����
            if left>right:
                return None
            # max�����ثe�o�q�̤j�ȩҦb��index
            max = left
            for i in range(left+1, right+1):
                if nums[i]>nums[max]:
                    max = i
            # �N�̤j�ȫئ�node
            node = TreeNode(val = nums[max])
            # ���l�|�O���䨺�q�̤j��node
            node.left = build(left, max-1)
            # �k�l�|�O�k�䨺�ݳ̤j��node
            node.right = build(max+1, right)
            return node
        # �]�ѼƬOindex, array��index�q0�}�l, len(nums)-1����
        return build(0, len(nums)-1)

# By stack, time: O(n), space: O(n)
# �γ��stack�ӫ�tree, ���ӭ쥻�n�D���C����̤jvalue
# ���stack�O�@�Ӥ�����ƥu�|���W�λ���ƧǪ�stack
# �ӬO�ھڥثe���X�쪺val��W�Ӥj�٤p�@�۹������P�ʧ@, push��pop
# tree�����D�ئn�����n�Q�Q���γ��stack��
# �b��ƶq���h���ɭԦ]�����@������Ƶ��c�]�n��ɶ�, �ĪG�|��W���t
# �٨S����
# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
#         n = len(nums)
#         stk = list()
#         left, right = [-1]*n, [-1]*n
#         tree = [None]*n

#         for i in range(n):
#             tree[i] = TreeNode(nums[i])
#             while stk and nums[i] > nums[stk[-1]]:
#                 right[stk[-1]] = i
#                 stk.pop()
#             if stk:
#                 left[i] = stk[-1]
#             stk.append(i)
        
#         root = None
#         for i in range(n):
#             if left[i] == right[i] == -1:
#                 root = tree[i]
#             elif right[i] == -1 or (left[i] != -1 and nums[left[i]] < nums[right[i]]):
#                 tree[left[i]].right = tree[i]
#             else:
#                 tree[right[i]].left = tree[i]
        
#         return root

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
