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

# 給k個已排序過的linklist, 要求將這k個linklist merge在一起且linklist一樣根據val由小到大排序

# By traversal all linklist, time: O(kn*logkn), space: O(kn)
# 實際上好像還是這個比dac快?! 還更省空間
# 其中k代表k個linklist, n代表k個linklist中最長的長度, kn即是兩者相乘
# 所以time = O(kn*logkn)是因為走訪所有linklist花O(kn), 而排序這kn個資料花O(kn*logkn)
# 這個方法可以用heapq和heapq.heapify()最佳化
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp = []
        # 記得對一個收到一個linklist時實際上是收到他們的head node位置
        for curi in lists:
            # 對每個linklist做走訪
            while curi:
                # 用tmp將所有linklist的val存起來
                tmp.append(curi.val)
                curi = curi.next
        # sort後要開始新建一個linklist將tmp內所有內容放進去
        tmp.sort()
        head = ListNode()
        curr = head
        # 新的linklist數量就是tmp元素數量
        for i in range(len(tmp)):
            # 將tmp內所有元素一個個接到新的linklist後頭
            curr.next = ListNode(val = tmp[i])
            curr = curr.next
        # head本身沒接, 是從head後開始接tmp內元素, 所以return head.next
        return head.next
        
# By divide and conquer, time: O(kn*logk), space: O(logk)
# 用divide and conquer做到每兩兩合併, 減少需要判斷的node數量, 省下複雜度
# class Solution:
#     # 一樣是合併兩linklist之code作為函式
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
    
#     # 不斷遞迴dac, 直到剩一個linklist或超出範圍才合併
#     def dac(self,lists,l,r):
#         # 終止條件, 剩一個linklist時回傳
#         if l==r:
#             return lists[l]
#         # 當l>r代表超出想判斷的範圍
#         # Ex: 原本期望第0個和第1個合併, l>r代表第1個和第0個合併, 但(0, 1)已經做過了不需要(1, 0)
#         if l>r:
#             return None
#         # m作為下次要遞迴的邊界
#         m = (l+r)//2
#         # 等同於在遞迴下去之後直到兩兩相鄰的linklist才會開始return(實際做merge2Lists)
#         return self.merge2Lists(self.dac(lists, l, m), self.dac(lists, m+1, r))

#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         n = len(lists)
#         if n==0:
#             return None
#         if n==1:
#             return lists[0]
#         return self.dac(lists, 0, len(lists)-1)

# By compare all linklist node, time: O(k^2*n), space: O(1), n代表linklist長度
# time = O(k^2*n)是因為res原本長度n, 第一次合併後變2n, 第i次合併變i*n
# 而合併會做k-1次所以2+..+k-1, 為O(k^2)
# 已知當只有兩個linklist時, 可以先創建一個head
# 接著從頭兩兩比對兩linklist當時node的val, 選擇將val較小者一一接到後面, 再比較下一次
# 但k個無法一次比較k個, 那就將k個linklist依序兩兩比較即可
# 這個做法有兩兩性質, 因此可以用divide and conquer做, time變成O(kn*logk), space變成O(logk)為recursive使用的stack空間
# 之後有機會做divide and conquer版, 不然現在這種複雜度過高
# class Solution:
#     # 將兩兩合併linklist作為函式
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

