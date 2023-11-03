#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive
class Solution:
    def inOrder(self, root:TreeNode, res):
        #遞迴的終止條件, 當非node時不用遞迴
        if root == None:
            return
        #inorder是左->中->右, 所以對每個node都是從左邊開始遞迴
        #先對左子樹做遞迴
        self.inOrder(root.left, res)
        #左子樹遞迴完成後才會輪到root
        #將root放入res
        res.append(root.val)
        #左子樹的部分和root都完成, 再對右子樹做遞迴
        self.inOrder(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #因回傳的是陣列, 且當只有一個node時要回傳空, 所以初始化一個陣列
        #從root開始對tree的每個node下去遞迴, 每次以當時的node為root做inorder
        res = []
        #開始做inorder追蹤
        self.inOrder(root, res)
        return res

# By stack
# #能用recursive就能用stack做
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         #維護一個叫做stack的list
#         # 因為append是從最尾端加入後進資料, 而pop是將最尾端資料取出
#         # 兩個配合即可達成後進先出的stack
#         stack = []
#         res = []
#         while root or stack:
#             if root:
#                 stack.append(root)
#                 root = root.left
#             else:
#                 cur = stack.pop()
#                 res.append(cur.val)
#                 root = cur.right
#         return res

# @lc code=end

