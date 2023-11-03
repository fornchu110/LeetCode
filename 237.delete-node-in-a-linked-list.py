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
# 因需要刪node又不給head, 也不要return, 所以只知道什麼val的node需要被刪掉
# 這樣的話刪掉方法就是把要被刪掉的node.val改成下個node的val
# 改完後直接跳過下個node, 這樣就不會知道其存在了
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 為何不能node = node.next? 因為上個node是指著目前node的位置
        # 就算node = node.next讓node這個pointer指向下個node, 但上個node仍然指向node原本的位置沒改變
        # 並沒有達到刪除node的作用, *node = *node->next才有意義, 但python沒有這寫法
        node.val = node.next.val
        node.next = node.next.next

# @lc code=end

