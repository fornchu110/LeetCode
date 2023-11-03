<<<<<<< HEAD
#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# ��preorder�Minorder���Xtree�����G, return�쥻tree���Ҽ�

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n)
# �z�Lpreorder��root, �A�hinorder����root��index
# inorder��root index�H���N�O��sub tree, �H�k�N�O�ksubtree
class Solution:
      def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # �פ����, tree���Ů�
        if not preorder or not inorder:
            return None
        # preorder���Ĥ@�Ӥ����@�w��Utree��root
        rootVal = preorder[0]
        # �Ы�root
        root = TreeNode(rootVal)
  
        # �hinorder����root�Ҧbindex
        midIndex = inorder.index(rootVal)

        # ��Xinorder�����l�M�k�l
        # index�H���O��sub tree, index�H�k�O�ksub tree
        # �ҥH���l�϶��O[0,midIndex),�k�l�϶��O[midIndex+1�An-1]
        inorderLeft = inorder[:midIndex]
        inorderRight = inorder[midIndex + 1:]
  
        # ��Xpreorder�����l�M�k�l
        # preorder�Minorder����sub tree�M�ksub tree���׬۵�
        # �]���z�L�e�����쪺inorder���ksubtree���ױo��preorder���ksubtree��m
        # preorder: root, ��sub tree�Ӥ���, �ksubtree�Ӥ���
        # root�O��0��, ��sub�O��1~1+��sub
        preorderLeft = preorder[1:len(inorderLeft)+1]
        # �ksub�O�ѤU������, �L��preorder�٬Oin
        preorderRight = preorder[len(inorderLeft)+1:]

        # �W���w�g���subtree��preorder�Minorder, �N�i�H��recursive
        # recursive���X��sub tree
        root.left = self.buildTree(preorderLeft, inorderLeft)
        # recursive���X�ksub tree
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
# ��preorder�Minorder���Xtree�����G, return�쥻tree���Ҽ�

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n)
# �z�Lpreorder��root, �A�hinorder����root��index
# inorder��root index�H���N�O��sub tree, �H�k�N�O�ksubtree
class Solution:
      def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # �פ����, tree���Ů�
        if not preorder or not inorder:
            return None
        # preorder���Ĥ@�Ӥ����@�w��Utree��root
        rootVal = preorder[0]
        # �Ы�root
        root = TreeNode(rootVal)
  
        # �hinorder����root�Ҧbindex
        midIndex = inorder.index(rootVal)

        # ��Xinorder�����l�M�k�l
        # index�H���O��sub tree, index�H�k�O�ksub tree
        # �ҥH���l�϶��O[0,midIndex),�k�l�϶��O[midIndex+1�An-1]
        inorderLeft = inorder[:midIndex]
        inorderRight = inorder[midIndex + 1:]
  
        # ��Xpreorder�����l�M�k�l
        # preorder�Minorder����sub tree�M�ksub tree���׬۵�
        # �]���z�L�e�����쪺inorder���ksubtree���ױo��preorder���ksubtree��m
        # preorder: root, ��sub tree�Ӥ���, �ksubtree�Ӥ���
        # root�O��0��, ��sub�O��1~1+��sub
        preorderLeft = preorder[1:len(inorderLeft)+1]
        # �ksub�O�ѤU������, �L��preorder�٬Oin
        preorderRight = preorder[len(inorderLeft)+1:]

        # �W���w�g���subtree��preorder�Minorder, �N�i�H��recursive
        # recursive���X��sub tree
        root.left = self.buildTree(preorderLeft, inorderLeft)
        # recursive���X�ksub tree
        root.right = self.buildTree(preorderRight, inorderRight)
        return root

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
