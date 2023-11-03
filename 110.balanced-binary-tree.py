<<<<<<< HEAD
#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# 給一個tree, return此tree是否平衡, 平衡代表最低height和最高height相差不超過1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive(bottom up), time: O(n) , space: O(n)
# space = O(n)來自recursive之stack消耗, tree最高深度最就n
# 相當於後序走訪, 得到結果後依照結果做判斷決定要return什麼
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # height同時算出深度和判斷是否平衡, 不平衡的子樹高度會是-1
        def height(root: TreeNode) -> int:
            if not root:
                return True
            # 先確認左右子樹是否平衡以及左右子樹的高度
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            # 只要左右子樹高度相差超過1就return -1, 左右其中是-1代表已經不平衡, 所以也是return -1
            if leftHeight==-1 or rightHeight==-1 or abs(leftHeight-rightHeight)>1:
                return -1
            # 既然平衡那多了node這個點高度就會是左右子樹較大者+1
            else:
                return max(leftHeight, rightHeight)+1
        # -1代表不平衡, 所以只要return>=0就代表平衡
        return height(root)>=0

# By recursive(top down), time: O(n^2) , space: O(n)
# 相當於前序走訪, 這個方法對每個子tree都會對其所有node確認height
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         # 單純計算當下root之tree最大高度
#         def height(root: TreeNode) -> int:
#             if not root:
#                 return 0
#             # 當下tree之最大高度就是左右子樹最大高度+1個root, 也就是+1
#             return max(height(root.left), height(root.right))+1
#         if not root:
#             return True
#         # 只要左右子樹平衡且左右子樹高度差在1以內代表整顆tree平衡
#         return abs(height(root.left)-height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
# @lc code=end

=======
#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# 給一個tree, return此tree是否平衡, 平衡代表最低height和最高height相差不超過1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive(bottom up), time: O(n) , space: O(n)
# space = O(n)來自recursive之stack消耗, tree最高深度最就n
# 相當於後序走訪, 得到結果後依照結果做判斷決定要return什麼
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # height同時算出深度和判斷是否平衡, 不平衡的子樹高度會是-1
        def height(root: TreeNode) -> int:
            if not root:
                return True
            # 先確認左右子樹是否平衡以及左右子樹的高度
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            # 只要左右子樹高度相差超過1就return -1, 左右其中是-1代表已經不平衡, 所以也是return -1
            if leftHeight==-1 or rightHeight==-1 or abs(leftHeight-rightHeight)>1:
                return -1
            # 既然平衡那多了node這個點高度就會是左右子樹較大者+1
            else:
                return max(leftHeight, rightHeight)+1
        # -1代表不平衡, 所以只要return>=0就代表平衡
        return height(root)>=0

# By recursive(top down), time: O(n^2) , space: O(n)
# 相當於前序走訪, 這個方法對每個子tree都會對其所有node確認height
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         # 單純計算當下root之tree最大高度
#         def height(root: TreeNode) -> int:
#             if not root:
#                 return 0
#             # 當下tree之最大高度就是左右子樹最大高度+1個root, 也就是+1
#             return max(height(root.left), height(root.right))+1
#         if not root:
#             return True
#         # 只要左右子樹平衡且左右子樹高度差在1以內代表整顆tree平衡
#         return abs(height(root.left)-height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
