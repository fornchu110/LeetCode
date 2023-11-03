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

# By recursive, time: O(n^2), space: O(n), n是len(nums)
# 給array, 每次選array中最大值當node, 再來左子為最大值所在index左半arr, 右子為最大值所在index右半arr
# 因每輪都要走訪找尋最大值, 所以當nums排序過那就是最壞情況
# 要以index作為參數傳遞和終止條件
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # left、right、max是存取nums用的index
        def build(left, right):
            # 終止條件
            # index一定是從小到大, 當給的陣列範圍index變成大到小, 就代表結束
            if left>right:
                return None
            # max紀錄目前這段最大值所在的index
            max = left
            for i in range(left+1, right+1):
                if nums[i]>nums[max]:
                    max = i
            # 將最大值建成node
            node = TreeNode(val = nums[max])
            # 左子會是左邊那段最大的node
            node.left = build(left, max-1)
            # 右子會是右邊那端最大的node
            node.right = build(max+1, right)
            return node
        # 因參數是index, array的index從0開始, len(nums)-1結束
        return build(0, len(nums)-1)

# By stack, time: O(n), space: O(n)
# 用單調stack來建tree, 不照原本要求的每輪找最大value
# 單調stack是一個內部資料只會遞增或遞減排序的stack
# 而是根據目前走訪到的val比上個大還小作相對應不同動作, push或pop
# tree相關題目好像都要想想怎麼用單調stack做
# 在資料量不多的時候因為維護複雜資料結構也要花時間, 效果會比上面差
# 還沒看懂
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

# By recursive, time: O(n^2), space: O(n), n是len(nums)
# 給array, 每次選array中最大值當node, 再來左子為最大值所在index左半arr, 右子為最大值所在index右半arr
# 因每輪都要走訪找尋最大值, 所以當nums排序過那就是最壞情況
# 要以index作為參數傳遞和終止條件
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # left、right、max是存取nums用的index
        def build(left, right):
            # 終止條件
            # index一定是從小到大, 當給的陣列範圍index變成大到小, 就代表結束
            if left>right:
                return None
            # max紀錄目前這段最大值所在的index
            max = left
            for i in range(left+1, right+1):
                if nums[i]>nums[max]:
                    max = i
            # 將最大值建成node
            node = TreeNode(val = nums[max])
            # 左子會是左邊那段最大的node
            node.left = build(left, max-1)
            # 右子會是右邊那端最大的node
            node.right = build(max+1, right)
            return node
        # 因參數是index, array的index從0開始, len(nums)-1結束
        return build(0, len(nums)-1)

# By stack, time: O(n), space: O(n)
# 用單調stack來建tree, 不照原本要求的每輪找最大value
# 單調stack是一個內部資料只會遞增或遞減排序的stack
# 而是根據目前走訪到的val比上個大還小作相對應不同動作, push或pop
# tree相關題目好像都要想想怎麼用單調stack做
# 在資料量不多的時候因為維護複雜資料結構也要花時間, 效果會比上面差
# 還沒看懂
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
