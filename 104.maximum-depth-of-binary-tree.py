#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# 給一個二元樹, return此樹的最深高度, root高度 = 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS(recursive) , time: O(n), space: O(h), h為tree高, 因recursive需要stack, 而stack大小取決recursive的深度, 最壞其況就是O(n)
# 用dfs走訪node, 最後將lev最深者return即可
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 自己的寫法, 使用nonloval
        # is用來判斷記憶體位置, ==用來判斷值
        if root is None:
             return 0
        # res初始化為0
        res = 0
        def dfs(node, lev):
            if node==None:
                return None
            # 因dfs這個函式要更改上一層, 也就是maxDepth這個所定義的變數res
            # 因此要先將res宣告成nonlocal
            # 如果res是在solution外也就是global, 那就要改成宣告global res才能修改
            nonlocal res
            # 走訪到了新的一層node, 所以lev+1
            lev += 1
            max(res, lev)
            dfs(node.left, lev)
            dfs(node.right, lev)
        # 為何lev從0開始?把lev想成走訪node之前所擁有的高度
        dfs(root, 0)
        return res

        #簡潔寫法, 不用寫額外函式
        # if root is None:
        #     # 這裡同時擔當初始化沒結點=高度0這件事
        #     return 0
        # # 不斷遞迴maxDeapth即可
        # l_depth = self.maxDepth(root.left)
        # r_depth = self.maxDepth(root.right)
        # # 整個tree的高度就是子tree中更高者+1
        # return max(l_depth, r_depth)+1

# By BFS(iterative), time: O(n), space: O(n)
# space = O(n)是因為維護queue花費的空間
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         # 空tree高度就是0
#         if root == None:
#             return 0
#         # 初始化queue和高度, 非空tree時從root開始走訪
#         # 這裡的queue實際上就是用list模擬, 通過append加入尾端, pop(0)將頭端拿出
#         # 代表list也能夠模擬stack
#         queue = [root]
#         depth = 0
#         # 當queue非空, 也就是還有node未走訪
#         while queue:
#             # 當前level的node數
#             n = len(queue)
#             # 將當前level的node一個一個處理
#             for i in range(n):
#                 node = queue.pop(0)
#                 # 如果有左子就將左子放入queue
#                 if node.left:
#                     queue.append(node.left)
#                 # 如果有右子就將右子放入queue
#                 if node.right:
#                     queue.append(node.right)
#             # 當前level的node pop完代表結束這層, 到下一層所以要+1
#             depth += 1
#         return depth

# @lc code=end

