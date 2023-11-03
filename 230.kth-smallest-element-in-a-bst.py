#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# 給一個BST, 要求return BST中第k小的數

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS(recursive), time: O(n), space: O(n)
# 先不管BST的特性直接走訪一遍拿到各個node的val, 排序後return第k小
# 雖然寫的有考慮特性而不用排序, 但有更多不用走訪n個node的做法, 以後再想
class Solution:
    # 第一個是nonlocal的作法, 將DFS寫成子函式
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 在外面宣告res
        res = []
        def DFS(node):
            # 裡面宣告res是nonlocal, 使走訪過程能將走訪到的node.val加入res
            nonlocal res
            # 終止條件, 非node就return
            if node is None:
                return 
            # 考慮BST特性的話, 可以發現BST用inorder走訪結果就剛好是有序數列
            # recursive左子->做node要做的事->recursive右子
            DFS(node.left)
            # 是node就將val加入res, 並且繼續往左子和右子走訪
            res.append(node.val)
            DFS(node.right)
        # 從root開始recursive
        DFS(root)
        # 將res第1小的就是第0個, 所以return res[k-1]
        return res[k-1]
    
    # 將DFS寫在外面, 也就是作為class中另一個函式的寫法 
    # 因為res是在別的函式定義, 所以要透過參數傳遞
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
