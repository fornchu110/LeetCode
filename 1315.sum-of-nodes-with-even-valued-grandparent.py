#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# By dfs, time: O(n), space: O(n)
# 將祖父的val為偶數之node.val加總return
# 因此要記錄祖父和parent的value做參數傳遞
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        # 祖父和parent的val都要當參數傳遞才能判斷
        def dfs(gp_val, p_val, node):
            if not node:
                return
            # 判斷祖父.val為偶數時, 將自身val加總
            if gp_val&1 == 0:
                nonlocal res
                res += node.val
            # 往下遞洄, 此時自身的parent變成child的祖父, 自身變成child的parent
            dfs(p_val, node.val, node.left)
            dfs(p_val, node.val, node.right)
        # root沒有parent和祖父, 初始化成-1不影響判斷
        dfs(-1, -1, root)
        return res

# By bfs, time: O(n), space: O(n)
# bfs的做法要維護queue才能知道目前level是否走訪完畢
# class Solution:
#     def sumEvenGrandparent(self, root: TreeNode) -> int:
#         q = collections.deque([root])
#         res = 0
#         while len(q) > 0:
#             node = q.popleft()
#             if node.val&1 == 0:
#                 if node.left:
#                     if node.left.left:
#                         res += node.left.left.val
#                     if node.left.right:
#                         res += node.left.right.val
#                 if node.right:
#                     if node.right.left:
#                         res += node.right.left.val
#                     if node.right.right:
#                         res += node.right.right.val
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         return res

# @lc code=end

