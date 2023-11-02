#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 計算node.val=自己+自己所有child的value平均數之node數量
# 這種題目的基本一定是用recursive做dfs走訪所有node做計算

# By DFS, Time: O(n), Space: O(logn)
# space = O(logn)是因為Recursive中stack花費的空間, 但這題只是二元樹有可能最差O(n), 所以O(height), height = 樹高比較準確
# 用DFS下去只是要同時記錄和和目前走過的數量, 一次回傳兩個參數
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root: Optional[TreeNode]):
            # 因用到dfs上一層函數averageOfSubtree所定義的res
            # 所以使用nonlocal, 這樣就能修改res了
            # 不想用nonlocal的話把res換成self.res
            nonlocal res 
            if not root:
                return 0, 0
            #對左右子樹做遞迴
            lsub = dfs(root.left)
            rsub = dfs(root.right)
            # 求出自己+自己所有child之value和
            value = lsub[0]+rsub[0]+root.val
            # 求出自己+自己所有child之node數量
            count = lsub[1]+rsub[1]+1
            # 看自己的value是否自己+自己所有child的value平均數
            # 若相等則+1
            if root.val == value // count:
                res += 1
            return value, count    
        dfs(root)
        return res
    
# By DFS, Time: O(n), Space: O(logn)
# 改成將def和res寫在class下
# class Solution:
#     def __init__(self):
#         self.res = 0
    
#     def dfs(self, root):
#         if not root:
#             return 0, 0
#         lsub = self.dfs(root.left)
#         rsub = self.dfs(root.right)
#         value = lsub[0]+rsub[0]+root.val
#         count = lsub[1]+rsub[1]+1
#         if root.val==value//count:
#             self.res += 1
#         return value, count

#     def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
#         self.dfs(root)
#         return self.res

             
# @lc code=end

