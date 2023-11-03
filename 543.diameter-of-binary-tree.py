<<<<<<< HEAD
#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# 給一個tree, return此tree中任兩點最長的path長度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS, time: O(n), space: O(height)
# space = O(height)是因recursive所需要的stack空間, 也就是recursive深度, 在tree就是樹高
# path長度是經過的node數-1
# 最長路徑會由root的左subtree最長+右subtree最長所組成
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 1
        # 找出左tree最長(也就是最深)的路徑和右tree最長路徑之和
        def depth(node):
            nonlocal res
            # 終止條件, 當非node時return
            if node is None:
                return 0
            # 找左子tree深度
            L = depth(node.left)
            # 找右子tree深度
            R = depth(node.right)
            # 將兩者相加, 並+上root本身所以+1
            # res是nonlocal的, 遞迴過程不用return res也在不斷更新
            res = max(res, L+R+1)
            # 遞迴過程要return的是該node左右子tree最大深度
            return max(L, R)+1
        # 以root為出發點
        depth(root)
        return res-1
        
# @lc code=end

=======
#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# 給一個tree, return此tree中任兩點最長的path長度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By DFS, time: O(n), space: O(height)
# space = O(height)是因recursive所需要的stack空間, 也就是recursive深度, 在tree就是樹高
# path長度是經過的node數-1
# 最長路徑會由root的左subtree最長+右subtree最長所組成
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 1
        # 找出左tree最長(也就是最深)的路徑和右tree最長路徑之和
        def depth(node):
            nonlocal res
            # 終止條件, 當非node時return
            if node is None:
                return 0
            # 找左子tree深度
            L = depth(node.left)
            # 找右子tree深度
            R = depth(node.right)
            # 將兩者相加, 並+上root本身所以+1
            # res是nonlocal的, 遞迴過程不用return res也在不斷更新
            res = max(res, L+R+1)
            # 遞迴過程要return的是該node左右子tree最大深度
            return max(L, R)+1
        # 以root為出發點
        depth(root)
        return res-1
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
