#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n), space是recursive所花費的stack, 為tree最大高度
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 終止條件, 當order為空時代表不是node
        if not inorder or not postorder:
            return None
        # root必定是postorder最後一個元素
        root_val = postorder[-1]
        # 建立root node
        root = TreeNode(root_val)
        # 找出root在inorder內的index, index以左是左sub tree, 以右是右sub tree
        midIndex = inorder.index(root_val)

        # 找出inorder下的左sub tree和右sub tree
        inorderLeft = inorder[:midIndex]
        inorderRight = inorder[midIndex+1:]

        # 找出postorder下的左sub tree和右sub tree, 長度都會和inorder相等
        # postorder: 左->右->root
        postorderLeft = postorder[: len(inorderLeft)]
        # -1是因為最後必定是root
        postorderRight = postorder[len(inorderLeft):len(inorder)-1]
        # recursive結果就是當下node之左child和右child
        # recursive 左sub tree
        root.left = self.buildTree(inorderLeft, postorderLeft)
        # recursive 右sub tree
        root.right = self.buildTree(inorderRight, postorderRight)
        # 想像一下recursive先遞後迴, child都確認了才能接到parent上
        # 所以在最後一刻才把root的left和right child接上
        # 所以仍然是return root, root已經透過上面的recursive和其他node串聯起來
        return root

# @lc code=end

