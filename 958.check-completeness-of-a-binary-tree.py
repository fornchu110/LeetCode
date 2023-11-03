#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# 給一個tree, 若tree是complete tree return True, 不是complete tree return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS and node index, time: O(n), space: O(n)
# perfect tree代表每個node只要有child必定會有兩個, 像是一個三角形
# full tree代表除了leaf外所有node都會有兩個child, 但可能最後一層不靠左
# complete tree則代表最後一個level不一定會全滿, 非leaf也可能只有1個child, 但最後一層全部靠左
# perfect = full and complete
# 判斷complete tree方式就是一層一層算index, 當index不等同目前tree中的node數時代表非complete
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # root的index是1
        idx = 1
        cnt = 0
        queue = collections.deque()
        # 將root和其index包成一個元素加入queue
        queue.append((root, idx))
        # BFS以level走訪, 只要還有node在queue代表尚未走訪完
        while queue:
            (node, idx) = queue.popleft()
            # pop一個node的同時代表走到一個node, cnt增加
            cnt += 1
            # 當node數不等同index代表非complete
            if cnt!=idx:
                return False
            # 避免node為None
            if node.left:
                # 左子的index是parent idx*2
                queue.append((node.left, 2*idx))
            if node.right:
                # 右子的index是parent idx*2+1
                queue.append((node.right, 2*idx+1))
        return True
        
# @lc code=end

