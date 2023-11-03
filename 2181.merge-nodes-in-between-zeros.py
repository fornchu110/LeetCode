<<<<<<< HEAD
#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By dummy node, time: O(n), space: O(1)
# �n�Nnode.val=0������node.val���[�`�ᰵ���@�ӷsnode
# �`�Nreturn�]�n�O��linklist��head
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        tmp = 0
        # �qhead.next�}�l�ҥH���γB�z�Ĥ@��val==0��node
        cur = head.next
        # �Ӳz�ӻ��o��cur�O����, �ҥH�[���[is not None�S���t�O, ���O����ЦӫD�Ȱ��P�_
        while cur is not None:
            if cur.val == 0:
                node = ListNode(tmp)
                # �Ĥ@��tail = dummy, �ҥHtail.next�P�ɵ���dummy.next
                # �n���γo�Ӱ��k��dummy�౵�W
                tail.next = node
                # tail����next�F, �H���ܰʥu��tail�b�ܰʤ��|���ʨ�dummy
                # �ҥH�̫ᤴ�i��dummy.next�Ӧ^��result��head
                tail = tail.next
                # �C���s�ؤF�@��node�n���U�@���[�`, tmp�n��l�Ƭ�0
                tmp = 0
            else:
                # �S�J��0��, ��node�Ȱ��[�`
                tmp += cur.val
            # �ݤU��node
            cur = cur.next
        return dummy.next

# @lc code=end

=======
#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By dummy node, time: O(n), space: O(1)
# �n�Nnode.val=0������node.val���[�`�ᰵ���@�ӷsnode
# �`�Nreturn�]�n�O��linklist��head
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        tmp = 0
        # �qhead.next�}�l�ҥH���γB�z�Ĥ@��val==0��node
        cur = head.next
        # �Ӳz�ӻ��o��cur�O����, �ҥH�[���[is not None�S���t�O, ���O����ЦӫD�Ȱ��P�_
        while cur is not None:
            if cur.val == 0:
                node = ListNode(tmp)
                # �Ĥ@��tail = dummy, �ҥHtail.next�P�ɵ���dummy.next
                # �n���γo�Ӱ��k��dummy�౵�W
                tail.next = node
                # tail����next�F, �H���ܰʥu��tail�b�ܰʤ��|���ʨ�dummy
                # �ҥH�̫ᤴ�i��dummy.next�Ӧ^��result��head
                tail = tail.next
                # �C���s�ؤF�@��node�n���U�@���[�`, tmp�n��l�Ƭ�0
                tmp = 0
            else:
                # �S�J��0��, ��node�Ȱ��[�`
                tmp += cur.val
            # �ݤU��node
            cur = cur.next
        return dummy.next

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
