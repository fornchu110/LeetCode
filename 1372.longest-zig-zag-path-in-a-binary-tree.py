<<<<<<< HEAD
#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# 給一binary tree, return此tree中最長的交錯path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS, time: O(n), space: O(1)
# 利用DFS遞迴, 從底部不斷更新答案至root
# 這題還可以用DP
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        # p_left代表著剛剛parent節點怎麼走下來, True代表是往左走下來, False代表是往右走下來
        def dfs(root: TreeNode, p_left: bool, long: int):
            nonlocal res
            # 終止條件
            if not root:
                # 非node不會增加path深度, 直接return即可
                return
            res = max(res, long)
            # 代表這次已經走過往左, 會兩方向都走訪
            if p_left:
                # 如果走過往左又再往左, 代表path重置, 因為沒交錯
                dfs(root.left, True, 1)
                # 走過往左這次選擇往右, 那path長度成功+1
                dfs(root.right, False, long+1)
            # 代表這次已經走過往右, 一樣會兩方向都走訪
            else:
                # 走過往右這次選擇往左, 那path長度成功+1
                dfs(root.left, True, long+1)
                # 走過往右選擇往右, 代表path重置
                dfs(root.right, False, 1)
        res = 0
        # 從root開始, 假設一開始決定要先往左
        # 為何不用往右?其實在dfs內考慮了, 畢竟從無到root實際上沒方向, 而且recursive兩個方向都會走訪
        dfs(root, True, 0)
        return res
    
# @lc code=end

=======
#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# 給一binary tree, return此tree中最長的交錯path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS, time: O(n), space: O(1)
# 利用DFS遞迴, 從底部不斷更新答案至root
# 這題還可以用DP
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        # p_left代表著剛剛parent節點怎麼走下來, True代表是往左走下來, False代表是往右走下來
        def dfs(root: TreeNode, p_left: bool, long: int):
            nonlocal res
            # 終止條件
            if not root:
                # 非node不會增加path深度, 直接return即可
                return
            res = max(res, long)
            # 代表這次已經走過往左, 會兩方向都走訪
            if p_left:
                # 如果走過往左又再往左, 代表path重置, 因為沒交錯
                dfs(root.left, True, 1)
                # 走過往左這次選擇往右, 那path長度成功+1
                dfs(root.right, False, long+1)
            # 代表這次已經走過往右, 一樣會兩方向都走訪
            else:
                # 走過往右這次選擇往左, 那path長度成功+1
                dfs(root.left, True, long+1)
                # 走過往右選擇往右, 代表path重置
                dfs(root.right, False, 1)
        res = 0
        # 從root開始, 假設一開始決定要先往左
        # 為何不用往右?其實在dfs內考慮了, 畢竟從無到root實際上沒方向, 而且recursive兩個方向都會走訪
        dfs(root, True, 0)
        return res
    
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
