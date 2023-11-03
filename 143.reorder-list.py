<<<<<<< HEAD
#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By reverse and fast-slow pointer, time: O(n), space: O(1)
# 要將link list依序頭尾重新排序 
# 原本想說直接走到tail再利用tail.next往前
# 但這樣做不行因沒反轉, tail.next實際上就是None
# 要先找出list的中點, 將中間以後的list反轉
# 利用fast-slow pointer的方式找mid
# 有list原本的head和反轉後那段list的head後, 將他們交錯合併即可
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
    # 利用fast slow pointer找mid
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        # 注意不能只判斷fast.next.next是因若fast.next為None, 無法判斷fast.next.next為何
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # fast走兩步slow走一步, fast不能走時slow剛好在mid
        return slow
    # 反轉後半部分link list
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur is not None:
            nextTemp = cur.next
            cur.next = prev
            prev = cur
            cur = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            cur1 = l1.next
            cur2 = l2.next
            l1.next = l2
            l1 = cur1
            l2.next = l1
            l2 = cur2
        

# @lc code=end

=======
#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By reverse and fast-slow pointer, time: O(n), space: O(1)
# 要將link list依序頭尾重新排序 
# 原本想說直接走到tail再利用tail.next往前
# 但這樣做不行因沒反轉, tail.next實際上就是None
# 要先找出list的中點, 將中間以後的list反轉
# 利用fast-slow pointer的方式找mid
# 有list原本的head和反轉後那段list的head後, 將他們交錯合併即可
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
    # 利用fast slow pointer找mid
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        # 注意不能只判斷fast.next.next是因若fast.next為None, 無法判斷fast.next.next為何
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # fast走兩步slow走一步, fast不能走時slow剛好在mid
        return slow
    # 反轉後半部分link list
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur is not None:
            nextTemp = cur.next
            cur.next = prev
            prev = cur
            cur = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            cur1 = l1.next
            cur2 = l2.next
            l1.next = l2
            l1 = cur1
            l2.next = l1
            l2 = cur2
        

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
