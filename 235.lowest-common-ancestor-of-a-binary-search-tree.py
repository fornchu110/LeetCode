#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# 給一binary search tree和兩node p、q, return他們的最低共同祖先
# 最低共同祖先就是高度最接近兩點的共同祖先, 記得要回傳node而非int

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# By iterative, time: O(n), space: O(1)
# 根據前面觀察到共同祖先的性質就是共同路徑的最後一個相同node後, 就了解其實可以同時走訪p和q
# Ex: p = 4: [6, 2, 4], q = 2: [6, 2]
# 所以使用while迴圈, 當p和q比當下的node小時往左走, 大時往右走
# 除此之外就代表已經沒有共同路徑可以往下走, break
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 初始化res為root
        res = root
        while True:
            # 只要能繼續走訪代表繼續有共同路徑, 那答案就更新成新走訪的node
            if p.val<res.val and q.val<res.val:
                res = res.left
            elif p.val>res.val and q.val>res.val:
                res = res.right
            # 沒有共同路徑能走下去了就break
            else:
                break
        return res

# By recursive, time: O(n), space: O(n)
# 可以發現甚麼叫做共同祖先?就是用同樣的方式走訪去查找兩個node時, 路徑裡最後一個相同的node
# Ex: 找2路徑:[6, 4, 2], 找4路徑: [6, 4], 那4就是4和2的共同祖先
# 因此分別查找兩node得到路徑後, 走訪路徑找最後一個相同node即可
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def DFS(node, target):
#             # 會更新在上層函式定義的path所以用nonlocal
#             nonlocal path
#             if node is None:
#                 return
#             # 這題要return node, 所以路徑裡是放node
#             path.append(node)
#             # 當找到目標node了就不繼續走訪
#             if node.val==target.val:
#                 return
#             # 目標比目前node小那就往左走訪
#             if node.val>target.val:
#                 DFS(node.left, target)
#             # 目標比目前node大那就往右走訪
#             elif node.val<target.val:
#                 DFS(node.right, target)
#         path = []
#         # p和q都是node
#         DFS(root, p)
#         p_path = path
#         path = []
#         DFS(root, q)
#         q_path = path
#         # 用zip同時走訪兩個路徑
#         for i, j in zip(p_path, q_path):
#             if i.val==j.val:
#                 res = i
#             # 一遇到不相同的node就break
#             else:
#                 break
#         return res

# @lc code=end

