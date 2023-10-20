#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ��k�Ӥw�ƧǹL��linklist, �n�D�N�ok��linklist merge�b�@�_�Blinklist�@�ˮھ�val�Ѥp��j�Ƨ�

# By traversal all linklist, time: O(kn*logkn), space: O(kn)
# ��ڤW�n���٬O�o�Ӥ�dac��?! �٧�٪Ŷ�
# �䤤k�N��k��linklist, n�N��k��linklist���̪�������, kn�Y�O��̬ۭ�
# �ҥHtime = O(kn*logkn)�O�]�����X�Ҧ�linklist��O(kn), �ӱƧǳokn�Ӹ�ƪ�O(kn*logkn)
# �o�Ӥ�k�i�H��heapq�Mheapq.heapify()�̨Τ�
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp = []
        # �O�o��@�Ӧ���@��linklist�ɹ�ڤW�O����L�̪�head node��m
        for curi in lists:
            # ��C��linklist�����X
            while curi:
                # ��tmp�N�Ҧ�linklist��val�s�_��
                tmp.append(curi.val)
                curi = curi.next
        # sort��n�}�l�s�ؤ@��linklist�Ntmp���Ҧ����e��i�h
        tmp.sort()
        head = ListNode()
        curr = head
        # �s��linklist�ƶq�N�Otmp�����ƶq
        for i in range(len(tmp)):
            # �Ntmp���Ҧ������@�ӭӱ���s��linklist���Y
            curr.next = ListNode(val = tmp[i])
            curr = curr.next
        # head�����S��, �O�qhead��}�l��tmp������, �ҥHreturn head.next
        return head.next
        
# By divide and conquer, time: O(kn*logk), space: O(logk)
# ��divide and conquer����C���X��, ��ֻݭn�P�_��node�ƶq, �٤U������
# class Solution:
#     # �@�ˬO�X�֨�linklist��code�@���禡
#     def merge2Lists(self,list1,list2):
#         head=ListNode(0)
#         curr_list=head
#         while list1 and list2:
#             if list1.val<list2.val:
#                 curr_list.next=list1
#                 list1=list1.next
#             else:
#                 curr_list.next=list2
#                 list2=list2.next
#             curr_list=curr_list.next
#         if list1:
#             curr_list.next=list1
#         if list2:
#             curr_list.next=list2
#         return head.next
    
#     # ���_���jdac, ����Ѥ@��linklist�ζW�X�d��~�X��
#     def dac(self,lists,l,r):
#         # �פ����, �Ѥ@��linklist�ɦ^��
#         if l==r:
#             return lists[l]
#         # ��l>r�N��W�X�Q�P�_���d��
#         # Ex: �쥻�����0�өM��1�ӦX��, l>r�N���1�өM��0�ӦX��, ��(0, 1)�w�g���L�F���ݭn(1, 0)
#         if l>r:
#             return None
#         # m�@���U���n���j�����
#         m = (l+r)//2
#         # ���P��b���j�U�h���᪽����۾F��linklist�~�|�}�lreturn(��ڰ�merge2Lists)
#         return self.merge2Lists(self.dac(lists, l, m), self.dac(lists, m+1, r))

#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         n = len(lists)
#         if n==0:
#             return None
#         if n==1:
#             return lists[0]
#         return self.dac(lists, 0, len(lists)-1)

# By compare all linklist node, time: O(k^2*n), space: O(1), n�N��linklist����
# time = O(k^2*n)�O�]��res�쥻����n, �Ĥ@���X�֫���2n, ��i���X����i*n
# �ӦX�ַ|��k-1���ҥH2+..+k-1, ��O(k^2)
# �w����u�����linklist��, �i�H���Ыؤ@��head
# ���۱q�Y������linklist���node��val, ��ܱNval���p�̤@�@����᭱, �A����U�@��
# ��k�ӵL�k�@�����k��, ���N�Nk��linklist�̧Ǩ�����Y�i
# �o�Ӱ��k�����ʽ�, �]���i�H��divide and conquer��, time�ܦ�O(kn*logk), space�ܦ�O(logk)��recursive�ϥΪ�stack�Ŷ�
# ���ᦳ���|��divide and conquer��, ���M�{�b�o�ؽ����׹L��
# class Solution:
#     # �N���X��linklist�@���禡
#     def merge2Lists(self,list1,list2):
#         head = ListNode(0)
#         curr_list=head
#         while list1 and list2:
#             if list1.val<list2.val:
#                 curr_list.next = list1
#                 list1 = list1.next
#             else:
#                 curr_list.next = list2
#                 list2 = list2.next
#             curr_list = curr_list.next
#         if list1:
#             curr_list.next = list1
#         if list2:
#             curr_list.next = list2
#         return head.next

#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         n = len(lists)
#         res=None
#         for i in range(n):
#             res=self.merge2Lists(res,lists[i])
#         return res

# @lc code=end

