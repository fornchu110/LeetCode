#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# 給一個tree, 希望做到以root為中心將左右子樹交換

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n), space來自recursive之stack消耗
# 因tree可能skewed也就是只有左child或只有右child, 所以最壞情況高度n, 代表著recursive n次, 所以space = O(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #input是以一個array儲存之tree的root
        #所以注意input不是一個array, 而是一個root node
        #所以實際上無論array內的排序, 題目已經把node之間的關係設定好了, 直接使用即可
        #因為是遞迴, 所以需要終止條件, 當走到非node時停止
        if not root:
            return root    
        #將input的所有node遞迴下去
        #也就是每到一個節點就當作root,將其左子點和右子點為root的子樹翻轉
        #讀到左子點
        left = self.invertTree(root.left)
        #讀到右子點
        right = self.invertTree(root.right)
        #將新的左子點另為原本的右子點, 將新的右子點另為原本的左子點
        root.left, root.right = right, left
        #retrun時回傳了一個已經做完交換的node
        #也就是說從最後一層node開始, 將交換完的node回傳給其parent, 直到回傳真正的root時結束
        return root

# @lc code=end

