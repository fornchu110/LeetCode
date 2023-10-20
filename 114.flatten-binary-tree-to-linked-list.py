#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By predecessor, time: O(n), space: O(1)
# 觀察preorder是root->左->右後, 發現左子樹最右的node被走訪後才開始走訪右子樹
# 所以左子樹最右node即是右子樹root的predecessor(前驅節點)
# 作法就是找到cur左子最右node後將root右子接上去
class Solution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                predecessor = nxt = cur.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = cur.right
                cur.left = None
                cur.right = nxt
            cur = cur.right

# By recursive, time: O(n), space: O(n)
# 先用preorder走訪後記錄下來順序, 再將node放到對應位置上
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         # 紀錄preorder結果
#         preorderList = list()
#         # 做preorder走訪
#         def preorderTraversal(root: TreeNode):
#             if root:
#                 #preorder順序:root必先->左子樹->右子樹
#                 preorderList.append(root)
#                 preorderTraversal(root.left)
#                 preorderTraversal(root.right)
        
#         preorderTraversal(root)
#         size = len(preorderList)
#         # 迭代方式調整node
#         for i in range(1, size):
#             prev, curr = preorderList[i - 1], preorderList[i]
#             prev.left = None
#             prev.right = curr

# @lc code=end

