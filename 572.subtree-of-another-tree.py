#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By enumerate DFS, time: O(|root| x |subroot|), space: O(max{droot ,dsubroot}), d指depth
# 對root那顆tree走訪以tree中所有node為root時
# 是否存在subroot為root的這顆tree作為subtree
# is是判斷記憶體位置, ==是判斷值, 雖然在None時都可以用, 但is會比較有效率
class Solution:
    # 兩者都往下走訪, 都是DFS
    # check用來看相同相對位置的node.val是否相等, 相等再繼續往下
    def check(self, curRoot, curSubRoot):
        # 當兩個tree在相同相對位置的node.val都為None代表正確
        if curRoot is None and curSubRoot is None:
            return True
        # 當一個是None一個不是代表不可能為subtree
        if curRoot is None or curSubRoot is None:
            return False
        # 需要上面兩個不能直接判斷curRoot.val==curSubRoot.val是因為None非值, 不能與值做==判斷
        # 當下兩個node值相等代表仍有可能是subTree, 再來看左子樹和右子樹, 都要相等所以用and
        return curRoot.val==curSubRoot.val and self.check(curRoot.left, curSubRoot.left) and self.check(curRoot.right, curSubRoot.right)
    
    # 用來看當下root是否存在subtree, 不斷呼叫check和自己
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        # 以原本root為root開始判斷, 若False便對原本root之左子樹以及右子樹做判斷 
        # 只要有其一發現是subTree即可所以用or, 是preorder順序做判斷: root->左子->右子
        return self.check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# @lc code=end

