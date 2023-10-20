#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# 倒tree, 璝tree琌complete tree return True, ぃ琌complete tree return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS and node index, time: O(n), space: O(n)
# perfect tree–node璶Τchildゲ﹚穦Τㄢ, 钩琌à
# full tree埃leaf┮Τnode常穦Τㄢchild, 程糷ぃ綼オ
# complete tree玥程levelぃ﹚穦骸, 獶leafΤ1child, 程糷场綼オ
# perfect = full and complete
# 耞complete treeよΑ碞琌糷糷衡index, 讽indexぃ单ヘ玡treeいnode计獶complete
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # rootindex琌1
        idx = 1
        cnt = 0
        queue = collections.deque()
        # 盢root㎝ㄤindexΘじqueue
        queue.append((root, idx))
        # BFSlevelǐ砐, 璶临Τnodequeue﹟ゼǐ砐Ч
        while queue:
            (node, idx) = queue.popleft()
            # popnodeǐnode, cnt糤
            cnt += 1
            # 讽node计ぃ单index獶complete
            if cnt!=idx:
                return False
            # 磷nodeNone
            if node.left:
                # オindex琌parent idx*2
                queue.append((node.left, 2*idx))
            if node.right:
                # index琌parent idx*2+1
                queue.append((node.right, 2*idx+1))
        return True
        
# @lc code=end

