<<<<<<< HEAD
#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#By recursive
class Solution:
    def preorder(self, root:TreeNode, res):
        # 非node就不用做遞迴了
        if not root:
            return 
        #前序:中->左->右
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
        return

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #回傳的是陣列, 所以一開始先做初始化
        res = []
        #由root開始遞迴整棵樹的node
        self.preorder(root, res)
        #遞迴全部完畢, 回傳前序追蹤結果res
        return res

    
        
# @lc code=end

=======
#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#By recursive
class Solution:
    def preorder(self, root:TreeNode, res):
        # 非node就不用做遞迴了
        if not root:
            return 
        #前序:中->左->右
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
        return

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #回傳的是陣列, 所以一開始先做初始化
        res = []
        #由root開始遞迴整棵樹的node
        self.preorder(root, res)
        #遞迴全部完畢, 回傳前序追蹤結果res
        return res

    
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
