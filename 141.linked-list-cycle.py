<<<<<<< HEAD
#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# By fast-slow pointer, time: O(n), space: O(1)
# 這個方法用於判斷cycle時, fast一次走兩步, slow一次走一步
# 若有cycle那fast總有一天會倒追到slow, 所以當fast==slow便代表cycle
# 若沒cycle, fast永遠比slow快直到走訪linklist完畢
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast = slow = head
        # 當fast還沒走訪完link list
        # 不能只while fast因fast一次走兩步, 若fast.next為空
        # 那fast.next無法指向fast.next.next 
        while fast and fast.next:
            # fast一次走兩步, slow一次走一步
            fast = fast.next.next
            slow = slow.next
            # 相等代表有cycle
            if fast==slow:
                return True
        return False

# By hashtable, time: O(n), space: O(n)因n個點要放n個進表才能查詢
# 每次走訪到新node去查是否連結到表內的node
# 有連結到表內代表cycle, return True 
# 走訪完了都沒cycle return false
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         # linklist內容不會重複用set, 會重複用list
#         res = set()
#         curr = head
#         while(curr!=None):
#             if curr.next in res:
#                 return True
#             res.add(curr)
#             curr = curr.next
#         return False

        
# @lc code=end

=======
#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# By fast-slow pointer, time: O(n), space: O(1)
# 這個方法用於判斷cycle時, fast一次走兩步, slow一次走一步
# 若有cycle那fast總有一天會倒追到slow, 所以當fast==slow便代表cycle
# 若沒cycle, fast永遠比slow快直到走訪linklist完畢
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast = slow = head
        # 當fast還沒走訪完link list
        # 不能只while fast因fast一次走兩步, 若fast.next為空
        # 那fast.next無法指向fast.next.next 
        while fast and fast.next:
            # fast一次走兩步, slow一次走一步
            fast = fast.next.next
            slow = slow.next
            # 相等代表有cycle
            if fast == slow:
                return True
        return False

# By hashtable, time: O(n), space: O(n)因n個點要放n個進表才能查詢
# 每次走訪到新node去查是否連結到表內的node
# 有連結到表內代表cycle, return True 
# 走訪完了都沒cycle return false
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         # linklist內容不會重複用set, 會重複用list
#         res = set()
#         curr = head
#         while(curr!=None):
#             if curr.next in res:
#                 return True
#             res.add(curr)
#             curr = curr.next
#         return False

        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
