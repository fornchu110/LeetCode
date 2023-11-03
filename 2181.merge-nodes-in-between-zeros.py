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
# 要將node.val=0之間的node.val做加總後做成一個新node
# 注意return也要是個linklist的head
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        tmp = 0
        # 從head.next開始所以不用處理第一個val==0的node
        cur = head.next
        # 照理來說這邊cur是指標, 所以加不加is not None沒有差別, 都是對指標而非值做判斷
        while cur is not None:
            if cur.val == 0:
                node = ListNode(tmp)
                # 第一次tail = dummy, 所以tail.next同時等於dummy.next
                # 要善用這個做法讓dummy能接上
                tail.next = node
                # tail換到next了, 以後變動只有tail在變動不會移動到dummy
                # 所以最後仍可用dummy.next來回傳result的head
                tail = tail.next
                # 每次新建了一個node要做下一輪加總, tmp要初始化為0
                tmp = 0
            else:
                # 沒遇到0時, 把node值做加總
                tmp += cur.val
            # 看下個node
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
# 要將node.val=0之間的node.val做加總後做成一個新node
# 注意return也要是個linklist的head
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        tmp = 0
        # 從head.next開始所以不用處理第一個val==0的node
        cur = head.next
        # 照理來說這邊cur是指標, 所以加不加is not None沒有差別, 都是對指標而非值做判斷
        while cur is not None:
            if cur.val == 0:
                node = ListNode(tmp)
                # 第一次tail = dummy, 所以tail.next同時等於dummy.next
                # 要善用這個做法讓dummy能接上
                tail.next = node
                # tail換到next了, 以後變動只有tail在變動不會移動到dummy
                # 所以最後仍可用dummy.next來回傳result的head
                tail = tail.next
                # 每次新建了一個node要做下一輪加總, tmp要初始化為0
                tmp = 0
            else:
                # 沒遇到0時, 把node值做加總
                tmp += cur.val
            # 看下個node
            cur = cur.next
        return dummy.next

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
