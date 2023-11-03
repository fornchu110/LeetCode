#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive dfs, time: O(n), space: O(n ) 
#一樣遞迴, 要看的是每節點的value就好
#深度優先搜索DFS
#BST左子更小右子更大
class Solution:
 def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        #遞迴終止條件
        if not root:
            return 0
        #當node比high還大, 右子一定也比high大不用找, 就要往更小的node找, 所以找左子
        if root.val>high:
            return self.rangeSumBST(root.left, low, high)
        #當node比low還小, 左子一定也比low小不用找, 就要往更大的node找, 所以找右子
        if root.val<low:
            return self.rangeSumBST(root.right, low, high)
        #找到適合的點, 也就是介於[low, high]便將其加入答案中, 且由於是之間所以左子右子都可能是答案
        return root.val+self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

# By bfs, time: O(n), space: O(n)
# class Solution:
#     def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
#         total = 0
#         q = collections.deque([root])
#         while q:
#             node = q.popleft()
#             if not node:
#                 continue
#             if node.val > high:
#                 q.append(node.left)
#             elif node.val < low:
#                 q.append(node.right)
#             else:
#                 total += node.val
#                 q.append(node.left)
#                 q.append(node.right)

#         return total

# @lc code=end

