<<<<<<< HEAD
#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# 給一個link list和k, 將link list中第k個元素跟到數第k個元素內容交換


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# By math and while, time: O(n), space: O(1)
# 先記錄好第一個node和第k個node, 利用相差k-1的性質
# 將兩個pointer同時右移直到原本指向第k個指標的pointer指向最後一個
# 此時原本指向第一個node的pointer便自然指向倒數第k個node, 再將兩者val交換即可
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 用left和right兩個指標初始化指向head
        left = right = head
        # 將right移動到link list中第k個node所在位置, 假如k=5要移動到此需要移動4次
        for i in range(k-1):
            right = right.next
        # 將第k個node的位置記錄起來
        forward = right
        # right和left同時右移到尾端, 這樣最後right到尾端時, left所在就是倒數第k個node
        # 因兩者都相差k-1的距離
        while right.next:
            left = left.next
            right = right.next
        # 倒數第k個node的位置記錄起來
        reverse = left
        # 交換兩者的value
        forward.val,reverse.val = reverse.val,forward.val
        return head

# @lc code=end

=======
#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# 給一個link list和k, 將link list中第k個元素跟到數第k個元素內容交換


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# By math and while, time: O(n), space: O(1)
# 先記錄好第一個node和第k個node, 利用相差k-1的性質
# 將兩個pointer同時右移直到原本指向第k個指標的pointer指向最後一個
# 此時原本指向第一個node的pointer便自然指向倒數第k個node, 再將兩者val交換即可
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 用left和right兩個指標初始化指向head
        left = right = head
        # 將right移動到link list中第k個node所在位置, 假如k=5要移動到此需要移動4次
        for i in range(k-1):
            right = right.next
        # 將第k個node的位置記錄起來
        forward = right
        # right和left同時右移到尾端, 這樣最後right到尾端時, left所在就是倒數第k個node
        # 因兩者都相差k-1的距離
        while right.next:
            left = left.next
            right = right.next
        # 倒數第k個node的位置記錄起來
        reverse = left
        # 交換兩者的value
        forward.val,reverse.val = reverse.val,forward.val
        return head

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
