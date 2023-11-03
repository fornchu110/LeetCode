<<<<<<< HEAD
#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# 給preorder和inorder走訪tree的結果, return原本tree的模樣

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n)
# 透過preorder找root, 再去inorder中找root的index
# inorder中root index以左就是左sub tree, 以右就是右subtree
class Solution:
      def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 終止條件, tree為空時
        if not preorder or not inorder:
            return None
        # preorder的第一個元素一定當下tree之root
        rootVal = preorder[0]
        # 創建root
        root = TreeNode(rootVal)
  
        # 去inorder中找root所在index
        midIndex = inorder.index(rootVal)

        # 找出inorder的左子和右子
        # index以左是左sub tree, index以右是右sub tree
        # 所以左子區間是[0,midIndex),右子區間是[midIndex+1，n-1]
        inorderLeft = inorder[:midIndex]
        inorderRight = inorder[midIndex + 1:]
  
        # 找出preorder的左子和右子
        # preorder和inorder之左sub tree和右sub tree長度相等
        # 因此透過前面的到的inorder左右subtree長度得到preorder左右subtree位置
        # preorder: root, 左sub tree個元素, 右subtree個元素
        # root是第0個, 左sub是第1~1+左sub
        preorderLeft = preorder[1:len(inorderLeft)+1]
        # 右sub是剩下的部分, 無論preorder還是in
        preorderRight = preorder[len(inorderLeft)+1:]

        # 上面已經找到subtree之preorder和inorder, 就可以做recursive
        # recursive走訪左sub tree
        root.left = self.buildTree(preorderLeft, inorderLeft)
        # recursive走訪右sub tree
        root.right = self.buildTree(preorderRight, inorderRight)
        return root

# @lc code=end

=======
#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# 給preorder和inorder走訪tree的結果, return原本tree的模樣

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n)
# 透過preorder找root, 再去inorder中找root的index
# inorder中root index以左就是左sub tree, 以右就是右subtree
class Solution:
      def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 終止條件, tree為空時
        if not preorder or not inorder:
            return None
        # preorder的第一個元素一定當下tree之root
        rootVal = preorder[0]
        # 創建root
        root = TreeNode(rootVal)
  
        # 去inorder中找root所在index
        midIndex = inorder.index(rootVal)

        # 找出inorder的左子和右子
        # index以左是左sub tree, index以右是右sub tree
        # 所以左子區間是[0,midIndex),右子區間是[midIndex+1，n-1]
        inorderLeft = inorder[:midIndex]
        inorderRight = inorder[midIndex + 1:]
  
        # 找出preorder的左子和右子
        # preorder和inorder之左sub tree和右sub tree長度相等
        # 因此透過前面的到的inorder左右subtree長度得到preorder左右subtree位置
        # preorder: root, 左sub tree個元素, 右subtree個元素
        # root是第0個, 左sub是第1~1+左sub
        preorderLeft = preorder[1:len(inorderLeft)+1]
        # 右sub是剩下的部分, 無論preorder還是in
        preorderRight = preorder[len(inorderLeft)+1:]

        # 上面已經找到subtree之preorder和inorder, 就可以做recursive
        # recursive走訪左sub tree
        root.left = self.buildTree(preorderLeft, inorderLeft)
        # recursive走訪右sub tree
        root.right = self.buildTree(preorderRight, inorderRight)
        return root

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
