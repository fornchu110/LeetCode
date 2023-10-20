#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By enumerate DFS, time: O(n?min(2^len+1 ,n)), space: O(height) 
# 要考慮到可能binary tree下的path有共同子路徑, 沒有都確認一遍無法確定是否不存在路徑
# 利用dfs走訪全部node確認是否存在路徑
# 主要想法是走訪每個node, 判定是否存在以當前node為root的path
# path上每個node都與給定的linklist之node值一對應
class Solution:
    def dfs(self, curHead, curRoot):
        # 當成功讀到linklist結束, 代表不用找了, path可行
        if curHead==None:
            return True
        # 當linklist還沒結束但tree結束了, 代表目前path只是一部份, 不可行
        if curRoot==None:
            return False
        # 當下tree node不等於預期的linklist node值時代表這條path不可行
        if curRoot.val!=curHead.val:
            return False
        # 不是前三種情況, 代表此path目前為止都正確, 要繼續看
        # 繼續看有兩種, 往左子樹看和往右子樹看, 只要其一path正確即可所以是用or
        return self.dfs(curHead.next, curRoot.left) or self.dfs(curHead.next, curRoot.right)
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # input至少有一個head且path判斷是由dfs內去做, 所以其實不用看head
        # if head==None:
        #     return True
        # 若沒有node能當root了linklist仍未結束, 代表此path失敗
        if root==None:
            return False
        # 除了從實際root開始做的dfs外(self.dfs(head, root))
        # 若前面node作為root的path失敗, 那再看以失敗點之左右child作為root的path是否存在
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

# @lc code=end

