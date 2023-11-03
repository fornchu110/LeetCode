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

# 給一個link list,[0, n]一對, [1, n-1]一對...以此類推
# return一對node.val相加最大值

# By list simulation, time: O(n), space: O(n)
# 走訪link list將value和index建成一個list
# 實際上利用list比操作link list更省時間, 不用做反轉等等操作
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        simulation = []
        cur = head
        # 將link list的val依序append到list中
        while cur:
            simulation.append(cur.val)
            cur = cur.next
        # 從第一個index和最後一個index開始做
        i, j = 0, len(simulation)-1
        # 初始化最大值
        res = 0
        while i<j:
            if simulation[i]+simulation[j]>res:
                res = simulation[i]+simulation[j]
            i += 1
            j -= 1
        return res

# By fast-slow pointer, time: O(n), space: O(1)
# 這種只要做node一半次數的要想到fast-slow pointer
# 利用fast-slow pointer走訪, 只反轉後半段的link list即可
# 不用複製, 更省時間空間
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         slow, fast = head, head.next
#         while fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         # slow會剛好指在前半linklist的最後一個node
#         # 反轉後半link list
#         last = slow.next
#         while last.next:
#             cur = last.next
#             last.next = cur.next
#             cur.next = slow.next
#             slow.next = cur
#         res = 0
#         # 完成後半反轉的同時, slow.next會剛好指在最後一個node
#         # 但因為已經反轉完畢, 所以slow.next的next會是倒數第二個node, 以此類推
#         x, y = head, slow.next
#         while y:
#             res = max(res, x.val + y.val)
#             x, y = x.next, y.next
#         return res

# By reverse and copy, time: O(n), space: O(n)
# linklist沒有index所以想到用反轉的, 先複製一份原本的list將其反轉
# 接著將沒反轉和有反轉的list同時對node.val做相加, 找出max
# 複製一份原因是若直接反轉就更改了link, 喪失原本link list
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         def copy(head):
#             cur = head
#             # 一開始dummy.next可以是head
#             dummy = ListNode(next = head)
#             prev = dummy
#             while cur:
#                 tmp = ListNode(val = cur.val, next = cur.next)
#                 # 第一輪的時候prev = dummy, 所以prev.next在這邊修改成tmp後
#                 # 同時也將dummy.next改為tmp
#                 prev.next = tmp
#                 prev = tmp
#                 cur = cur.next
#             return dummy.next
#         def reverse(head):
#             # 反轉的同時用cnt紀錄link list長度
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
#         # list1是原本link list的head, list2是反轉後link list的head
#         list1 = copy(head)
#         list2, cnt = reverse(head)
#         # 因兩兩一對看, 最後只需要做cnt//2次
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

