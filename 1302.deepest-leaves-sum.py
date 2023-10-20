#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive and nonlocal, time: O(n), space: O(n)
# 要將leave的val加總後return, 使用DFS的方式遞迴走訪整個tree
# 難點在於如何傳遞加總後的值res以及走訪
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # 使用到maxLeval判斷leave, res用來記錄leave總和
        maxLevel, res = -1, 0
        def dfs(node: Optional[TreeNode], level: int) -> None:
            # 終止條件
            # 記住node is None比not Node寫法更好, 不然會多判斷空的字串、列表、字典進來
            if node is None:
                return
            # 當函式內修改上一層函式的local variable是用nonlocal
            # 這邊就是因為使用到def deepestLeavesSum宣告的maxLevel和res
            # 若是global variable(最外層)不可再用nonlocal, 多此一舉
            # 函式內修改global variable才用global, 避免宣告並使用到一個新的local variable
            # global宣告是無論前後的, nonlocal則否
            # 注意單純使用應該是不用額外宣告的
            nonlocal maxLevel, res
            # 如果當下的層數比之前紀錄的更深, 代表之前的node都不會是leave
            # 重新assign maxLevel和res
            if level>maxLevel:
                maxLevel, res = level, node.val
            # 層數最深的node一定是leave, 所以先把最深的找出來加總
            elif level==maxLevel:
                res += node.val
            # 這層走訪完, 往下一層
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        # 將層數當作參數傳遞, 一邊走訪一邊知道到第幾層
        dfs(root, 0)
        return res
        
# @lc code=end

