<<<<<<< HEAD
#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By dfs, time: O(n), space: O(1)
# ―BSTい┮Τnodeぇval+よtree valぇ, 琌BST┮よ常琌valueゑぇnode
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        tmp = 0
        def dfs(node):
            if node is not None:
                # い秈ㄓ, 娩node常рvalue暗羆穝筁, 近オ娩node
                nonlocal tmp
                dfs(node.right)
                tmp += node.val
                node.val = tmp
                dfs(node.left)
        # 眖root秨﹍ǐ砐, い->->オ
        dfs(root)
        return root
        
# @lc code=end

=======
#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By dfs, time: O(n), space: O(1)
# ―BSTい┮Τnodeぇval+よtree valぇ, 琌BST┮よ常琌valueゑぇnode
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        tmp = 0
        def dfs(node):
            if node is not None:
                # い秈ㄓ, 娩node常рvalue暗羆穝筁, 近オ娩node
                nonlocal tmp
                dfs(node.right)
                tmp += node.val
                node.val = tmp
                dfs(node.left)
        # 眖root秨﹍ǐ砐, い->->オ
        dfs(root)
        return root
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
