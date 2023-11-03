#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# By in-place modify, time: O(1), space: O(1)
# �]�ݭn�Rnode�S����head, �]���nreturn, �ҥH�u���D����val��node�ݭn�Q�R��
# �o�˪��ܧR����k�N�O��n�Q�R����node.val�令�U��node��val
# �粒�᪽�����L�U��node, �o�˴N���|���D��s�b�F
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # ���󤣯�node = node.next? �]���W��node�O���ۥثenode����m
        # �N��node = node.next��node�o��pointer���V�U��node, ���W��node���M���Vnode�쥻����m�S����
        # �èS���F��R��node���@��, *node = *node->next�~���N�q, ��python�S���o�g�k
        node.val = node.next.val
        node.next = node.next.next

# @lc code=end

