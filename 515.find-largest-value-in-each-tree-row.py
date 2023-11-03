#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 給一Tree的root, retun一個list內容是tree內各個level中node.val最大值

# By BFS, time: O(n), space:o(n)
# 就是用BFS的方式走訪, 注意每level要記錄目前最大node.val即可
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        # 建立deque比list運作省時
        queue = collections.deque()
        queue.append(root)
        # 當queue還有元素就代表tree還沒走訪完
        while(len(queue)):
            # 要比較最大值, 所以先初始化一個負無限小
            maxtmp = float("-inf")
            # 每次走到這邊算的長度就是此level中node數
            n = len(queue)
            # 對後面n個node, 也就是此level的node
            for i in range(n):
                # 一一pop出來看值是否最大以及有child就加入queue
                tmpnode = queue.popleft()
                maxtmp = max(maxtmp, tmpnode.val)
                if tmpnode.left is not None:
                    queue.append(tmpnode.left)
                if tmpnode.right is not None:
                    queue.append(tmpnode.right)
            # 此level中所有node都看過值且他們的child都被加入queue
            # res內加入此level最大值
            res.append(maxtmp)
        return res


# @lc code=end

