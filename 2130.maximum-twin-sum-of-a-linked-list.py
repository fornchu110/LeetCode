#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ���@��link list,[0, n]�@��, [1, n-1]�@��...�H������
# return�@��node.val�ۥ[�̤j��

# By list simulation, time: O(n), space: O(n)
# ���Xlink list�Nvalue�Mindex�ئ��@��list
# ��ڤW�Q��list��ާ@link list��ٮɶ�, ���ΰ����൥���ާ@
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        simulation = []
        cur = head
        # �Nlink list��val�̧�append��list��
        while cur:
            simulation.append(cur.val)
            cur = cur.next
        # �q�Ĥ@��index�M�̫�@��index�}�l��
        i, j = 0, len(simulation)-1
        # ��l�Ƴ̤j��
        res = 0
        while i<j:
            if simulation[i]+simulation[j]>res:
                res = simulation[i]+simulation[j]
            i += 1
            j -= 1
        return res

# By fast-slow pointer, time: O(n), space: O(1)
# �o�إu�n��node�@�b���ƪ��n�Q��fast-slow pointer
# �Q��fast-slow pointer���X, �u�����b�q��link list�Y�i
# ���νƻs, ��ٮɶ��Ŷ�
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         slow, fast = head, head.next
#         while fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         # slow�|��n���b�e�blinklist���̫�@��node
#         # �����blink list
#         last = slow.next
#         while last.next:
#             cur = last.next
#             last.next = cur.next
#             cur.next = slow.next
#             slow.next = cur
#         res = 0
#         # ������b���઺�P��, slow.next�|��n���b�̫�@��node
#         # ���]���w�g���৹��, �ҥHslow.next��next�|�O�˼ƲĤG��node, �H������
#         x, y = head, slow.next
#         while y:
#             res = max(res, x.val + y.val)
#             x, y = x.next, y.next
#         return res

# By reverse and copy, time: O(n), space: O(n)
# linklist�S��index�ҥH�Q��Τ��઺, ���ƻs�@���쥻��list�N�����
# ���۱N�S����M�����઺list�P�ɹ�node.val���ۥ[, ��Xmax
# �ƻs�@����]�O�Y��������N���Flink, �ॢ�쥻link list
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         def copy(head):
#             cur = head
#             # �@�}�ldummy.next�i�H�Ohead
#             dummy = ListNode(next = head)
#             prev = dummy
#             while cur:
#                 tmp = ListNode(val = cur.val, next = cur.next)
#                 # �Ĥ@�����ɭ�prev = dummy, �ҥHprev.next�b�o��ק令tmp��
#                 # �P�ɤ]�Ndummy.next�אּtmp
#                 prev.next = tmp
#                 prev = tmp
#                 cur = cur.next
#             return dummy.next
#         def reverse(head):
#             # ���઺�P�ɥ�cnt����link list����
#             cnt = 0
#             prev = None
#             cur = head    
#             while cur:
#                 cnt += 1
#                 next = cur.next
#                 cur.next = prev
#                 prev = cur
#                 cur = next
#             return prev, cnt
#         # list1�O�쥻link list��head, list2�O�����link list��head
#         list1 = copy(head)
#         list2, cnt = reverse(head)
#         # �]���@���, �̫�u�ݭn��cnt//2��
#         n = cnt//2
#         cur1 = list1
#         cur2 = list2
#         res = 0
#         while n:
#             if cur1.val+cur2.val>max:
#                 res = cur1.val+cur2.val
#             cur1 = cur1.next
#             cur2 = cur2.next
#             n -= 1
#         return res
        
# @lc code=end

