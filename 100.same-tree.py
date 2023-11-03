<<<<<<< HEAD
#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# 給兩tree p和q, return 此兩樹是否相同

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS(recursive), time: O(min(P, Q)), time: O(min(P, Q)), P、Q分別代表p、q之node數
# min的原因是只要有一者提前是判斷完那就代表false
# 複雜度一樣但實際比較快
# 同時對兩個tree做BFS
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        # collections內實作了多種容器, .deque是雙邊queue, [p]代表從p之head開始將p一個個放入deque
        # 也可以用deque([p, 3])代表放入p中最早走訪到的3個node
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            # popleft等同用list實作時的pop[0]
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val!=node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            # 邊界條件, 利用XOR兩者相同為1, 兩者不同為0的性質
            # tree node因為是一個一個接的linklist, 不可用^判斷, 而None時又不能判斷val
            # 所以利用not, 兩者為空時兩者個not都會是True, 而兩者非空時兩者的not都會是False, 也就是說不同時條件才成立
            # 這種寫法也可以用在開頭判斷return False時
            if (not left1)^(not left2):
                return False
            if (not right1)^(not right2):
                return False
            # 有子node就分別加入queue內, 注意不能將None加入所以要判斷
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)
        # 走到這邊不可能兩邊都還有node, 兩邊都為空時希望return True
        # 所以才用not而且不需要XOR
        return not queue1 and not queue2

# By DFS(recursive), time: O(min(P, Q)), time: O(min(P, Q)), P、Q分別代表p、q之node數
# min的原因是只要有一者提前是判斷完那就代表false
# 兩邊同時做DPS比較
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         # 同時比較兩個tree要注意邊界條件, 因為None, 也就是當一邊為空時, 無法比較val
#         # 當兩邊都是None, 那沒有問題都一樣, 為True
#         if p is None and q is None:
#             return True
#         # 利用elif在這裡排除了兩邊都是空的狀況
#         # 當兩邊有其一為空另一邊不為空時, 代表不一樣, 為False
#         elif p is None or q is None:
#             return False
#         # 走到這邊代表兩邊都非空, 可以比較val, 當val不同代表不一樣
#         elif p.val!=q.val:
#             return False
#         # 這邊代表兩邊都非空且val相同, 那就比較兩邊的左子和右子
#         else:
#             lsub = self.isSameTree(p.left, q.left)
#             rsub = self.isSameTree(p.right, q.right)
#             # True或false, 直接在return判斷即可
#             # 不用賦予成lsub和rsub兩變數也能做判斷
#             return lsub and rsub
    
# @lc code=end

=======
#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# 給兩tree p和q, return 此兩樹是否相同

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By BFS(recursive), time: O(min(P, Q)), time: O(min(P, Q)), P、Q分別代表p、q之node數
# min的原因是只要有一者提前是判斷完那就代表false
# 複雜度一樣但實際比較快
# 同時對兩個tree做BFS
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        # collections內實作了多種容器, .deque是雙邊queue, [p]代表從p之head開始將p一個個放入deque
        # 也可以用deque([p, 3])代表放入p中最早走訪到的3個node
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            # popleft等同用list實作時的pop[0]
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val!=node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            # 邊界條件, 利用XOR兩者相同為1, 兩者不同為0的性質
            # tree node因為是一個一個接的linklist, 不可用^判斷, 而None時又不能判斷val
            # 所以利用not, 兩者為空時兩者個not都會是True, 而兩者非空時兩者的not都會是False, 也就是說不同時條件才成立
            # 這種寫法也可以用在開頭判斷return False時
            if (not left1)^(not left2):
                return False
            if (not right1)^(not right2):
                return False
            # 有子node就分別加入queue內, 注意不能將None加入所以要判斷
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)
        # 走到這邊不可能兩邊都還有node, 兩邊都為空時希望return True
        # 所以才用not而且不需要XOR
        return not queue1 and not queue2

# By DFS(recursive), time: O(min(P, Q)), time: O(min(P, Q)), P、Q分別代表p、q之node數
# min的原因是只要有一者提前是判斷完那就代表false
# 兩邊同時做DPS比較
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         # 同時比較兩個tree要注意邊界條件, 因為None, 也就是當一邊為空時, 無法比較val
#         # 當兩邊都是None, 那沒有問題都一樣, 為True
#         if p is None and q is None:
#             return True
#         # 利用elif在這裡排除了兩邊都是空的狀況
#         # 當兩邊有其一為空另一邊不為空時, 代表不一樣, 為False
#         elif p is None or q is None:
#             return False
#         # 走到這邊代表兩邊都非空, 可以比較val, 當val不同代表不一樣
#         elif p.val!=q.val:
#             return False
#         # 這邊代表兩邊都非空且val相同, 那就比較兩邊的左子和右子
#         else:
#             lsub = self.isSameTree(p.left, q.left)
#             rsub = self.isSameTree(p.right, q.right)
#             # True或false, 直接在return判斷即可
#             # 不用賦予成lsub和rsub兩變數也能做判斷
#             return lsub and rsub
    
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
