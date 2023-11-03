#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# 給一個tree, 要求retrun內各個元素是同一level之node.val
# Ex: 1是level1, 9、10是level2, return:[[1], [9, 10]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS(iterative), time: O(n), space: O(n)
# 要根據level就是用BFS, 只是要注意如何蒐集同level元素和何時append
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        # 將root新增進queue
        queue = collections.deque([root])
        res = []
        # 當queue還有元素代表尚未走訪完
        # 實際上每走完一個level會回到while這邊
        while queue:
            # 同level的元素要放在一起
            tmp = []
            # n代表著這一level的元素數量
            n = len(queue)
            for i in range(n):
                # pop n次, 也就是對同level所有node做處理
                node = queue.popleft()
                # 加入tmp
                tmp.append(node.val)
                ltree = node.left
                rtree = node.right
                # 如果有child就放入queue
                if ltree:
                    queue.append(ltree)
                if rtree:
                    queue.append(rtree)
            # 做完for代表著一個level結束, 將tmp加入res
            res.append(tmp)
        return res
        
# @lc code=end

