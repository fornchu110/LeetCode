#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By enumerate DFS, time: O(n?min(2^len+1 ,n)), space: O(height) 
# �n�Ҽ{��i��binary tree�U��path���@�P�l���|, �S�����T�{�@�M�L�k�T�w�O�_���s�b���|
# �Q��dfs���X����node�T�{�O�_�s�b���|
# �D�n�Q�k�O���X�C��node, �P�w�O�_�s�b�H��enode��root��path
# path�W�C��node���P���w��linklist��node�Ȥ@����
class Solution:
    def dfs(self, curHead, curRoot):
        # ���\Ū��linklist����, �N���Χ�F, path�i��
        if curHead==None:
            return True
        # ��linklist�٨S������tree�����F, �N��ثepath�u�O�@����, ���i��
        if curRoot==None:
            return False
        # ��Utree node������w����linklist node�ȮɥN��o��path���i��
        if curRoot.val!=curHead.val:
            return False
        # ���O�e�T�ر��p, �N��path�ثe������T, �n�~���
        # �~��ݦ����, �����l��ݩM���k�l���, �u�n��@path���T�Y�i�ҥH�O��or
        return self.dfs(curHead.next, curRoot.left) or self.dfs(curHead.next, curRoot.right)
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # input�ܤ֦��@��head�Bpath�P�_�O��dfs���h��, �ҥH��ꤣ�ά�head
        # if head==None:
        #     return True
        # �Y�S��node���root�Flinklist��������, �N��path����
        if root==None:
            return False
        # ���F�q���root�}�l����dfs�~(self.dfs(head, root))
        # �Y�e��node�@��root��path����, ���A�ݥH�����I�����kchild�@��root��path�O�_�s�b
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

# @lc code=end

