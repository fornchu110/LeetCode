#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By simulation and bitwise, time: O(n), space: O(1)
# �a����binary��decimal�L�{�p��, �`�N���ݭn�����X�@��list��node���O���U��
# ����snode, �N��e�����ȥ����L�h, �]�N�O*2, �ӵ��G�N�O�A�[�W��Unode.val
# �o�˰����Ψ��X�N�ٮɶ�, �]�٤U�Nnode.val�O���U�Ӫ��Ŷ�
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        res = 0
        while(cur!=None):
            #res = res*2+cur.val, �̪��[�����k
            #��binary�i�H����B��, bitwise�ާ@��[�ٮɶ�
            #<<1�N�����]�N�O*2�ĪG, |�ӥ[�Wcur.val
            res = (res<<1)|cur.val 
            cur = cur.next
        return res
        
# @lc code=end

