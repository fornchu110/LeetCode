#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# By choice, time: O(n), space: O(n)
# choice可以從陣列中等機率的隨機選擇一個元素
class Solution:
    # init會拿到作為linklist頭部node的head
    # init是使用作為此class的object都會必定有的
    # 所以外面任何測資給定linklist和其head後, 呼叫Solution便會執行下面內容
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        # 使用一個self.arr存放linklist內所有node
        self.arr = list()
        # 對linklist進行走訪, 並把node放到arr內
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        # 當外面作為Solution這一class的object呼叫.getRandom時
        # 便會使用choice從其所有node中隨機挑選一個node return
        return choice(self.arr)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

