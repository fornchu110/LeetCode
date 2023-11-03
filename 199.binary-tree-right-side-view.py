#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# 給一個tree, 要求return tree每一level最右邊的元素

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS, time: O(n), space: O(n)
# 用BFS走訪, 每次結束一個level將最尾端元素加入res即可
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        res = []
        queue = collections.deque([root])
        # 每處理一個level會判斷一次while
        while queue:
            # 用tmp儲存每一level之node.val
            tmp = []
            # n就是該level所有的node數量
            n = len(queue)
            # 避免處理到不同level的node
            for i in range(n):
                node = queue.popleft()
                # 記得要append的是node.val不是node
                tmp.append(node.val)
                # 不是None才要加入queue, 因為這樣才有value和child
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # queue有元素才會執行迴圈, 所以不用擔心tmp元素為空造成的out of range
            # 用tmp.pop()會更慢
            res.append(tmp[n-1])
        return res


# @lc code=end

