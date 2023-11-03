<<<<<<< HEAD
#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# 給一個tree, return tree中最廣的廣度是多少
# 記住寬度不等於每層節點數量, 而是該層最右邊和最左邊node之index差異

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS, time: O(n), space: O(n)
# 用array來儲存, 關鍵在於binary tree的parent和child之index關係
# 找出每層的寬度後求最大值, 寬度由每層最大編號node之index減去最小編號node之index+1得出
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 初始化array, 放入root此時是第一層, 最寬是1且root之index = 1
        res = 1
        # 每層會放入該層的node
        queue = collections.deque()
        # 記住append一次一個元素
        queue.append([root, 1])
        while queue:
            # 用tmp存放當下層數的node
            tmp = collections.deque()
            for node, index in queue:
                # 左子index會是parent index*2
                if node.left:
                    tmp.append([node.left, index*2])
                # 右子index會是parent index*2+1
                if node.right:
                    tmp.append([node.right, index*2+1])
            # 最大編號index-最小編號index, 如果比res還大就更新res
            # 上一層倒數第一個node(最右邊)的index-上一層第0個node(最左邊)的index+1
            res = max(res, queue[-1][1]-queue[0][1]+1)
            # 更新arr往下一層看, 若tmp為空代表這層沒node, 也就是已經沒有層能看了, 跳出迴圈
            queue = tmp
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# 給一個tree, return tree中最廣的廣度是多少
# 記住寬度不等於每層節點數量, 而是該層最右邊和最左邊node之index差異

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS, time: O(n), space: O(n)
# 用array來儲存, 關鍵在於binary tree的parent和child之index關係
# 找出每層的寬度後求最大值, 寬度由每層最大編號node之index減去最小編號node之index+1得出
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 初始化array, 放入root此時是第一層, 最寬是1且root之index = 1
        res = 1
        # 每層會放入該層的node
        queue = collections.deque()
        # 記住append一次一個元素
        queue.append([root, 1])
        while queue:
            # 用tmp存放當下層數的node
            tmp = collections.deque()
            for node, index in queue:
                # 左子index會是parent index*2
                if node.left:
                    tmp.append([node.left, index*2])
                # 右子index會是parent index*2+1
                if node.right:
                    tmp.append([node.right, index*2+1])
            # 最大編號index-最小編號index, 如果比res還大就更新res
            # 上一層倒數第一個node(最右邊)的index-上一層第0個node(最左邊)的index+1
            res = max(res, queue[-1][1]-queue[0][1]+1)
            # 更新arr往下一層看, 若tmp為空代表這層沒node, 也就是已經沒有層能看了, 跳出迴圈
            queue = tmp
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
