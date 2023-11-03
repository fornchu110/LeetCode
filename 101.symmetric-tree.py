<<<<<<< HEAD
#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# 給一tree, return此tree是否鏡像對稱

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n), recursive需要花費stack空間
# space = O(n)原因是recursive花費的stack空間就是recursive的深度, 在這邊就是指最高樹高, 而當所有node都只有一個child時就會高n
# 利用跟檢測兩tree是否相同類似的想法, 拿root的left和right出來檢測兩tree是否鏡像
# 這題給至少一個node, 所以不用判斷root為None
class Solution:
    # same寫在外面, 不知哪個快
    # def same(self, p, q):
    #     if p is None and q is None:
    #         return True
    #     elif p is None or q is None:
    #         return False
    #     elif p.val!=q.val:
    #         return False
    #     else:
    #         lsub = self.same(p.left, q.right)
    #         rsub = self.same(p.right, q.left)
    #         return lsub and rsub
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # same寫在裡面
        def same(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val!=q.val:
                return False
            else:
                # 鏡像, 也就是左子要=右子且右子=左子
                lsub = same(p.left, q.right)
                rsub = same(p.right, q.left)
                return lsub and rsub
        # 找出root的左右child, recursive下去判斷是否鏡像
        ltree = root.left
        rtree = root.right
        return same(ltree, rtree)

# By BFS(iterative), time: O(n), space: O(n)
# 雖然要同時判斷兩個tree, 但可以只用一個queue做到
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         rtree = root.right
#         ltree = root.left    
#         # 建立queue
#         queue = collections.deque()
#         # 因要一次看兩個tree, 所以將兩tree node包成一個元素append進去, append一次只能一個元素
#         # append進去的(rtree, ltree)就是當下要比較的兩個元素
#         queue.append((rtree, ltree))
#         while queue:
#             # twonode = queue.popleft()
#             # rtree = twonode[0]
#             # ltree = twonode[1]
#             # pop出來一次是(r, l)這樣的格式, 跟上面同樣意思, 注意不要pop兩次
#             # rtree, ltree等同於(rtree, ltree)
#             rtree, ltree = queue.popleft
#             # 兩者都是None代表不會有child, 直接continnue
#             if rtree is None and ltree is None:
#                 continue
#             elif rtree is None or ltree is None:
#                 return False
#             elif rtree.val!=ltree.val:
#                 return False
#             else:
#                 # 下次比較rtree的右子和ltree的左子
#                 queue.append((rtree.right, ltree.left))
#                 # 以及比較rtree的左子和ltree的右子
#                 queue.append((rtree.left, ltree.right))
#         # 跳出while代表queue沒有任何元素, 也就是已經走訪完兩個tree, 必定是True    
#         return True
        
# @lc code=end

=======
#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# 給一tree, return此tree是否鏡像對稱

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# By recursive, time: O(n), space: O(n), recursive需要花費stack空間
# space = O(n)原因是recursive花費的stack空間就是recursive的深度, 在這邊就是指最高樹高, 而當所有node都只有一個child時就會高n
# 利用跟檢測兩tree是否相同類似的想法, 拿root的left和right出來檢測兩tree是否鏡像
# 這題給至少一個node, 所以不用判斷root為None
class Solution:
    # same寫在外面, 不知哪個快
    # def same(self, p, q):
    #     if p is None and q is None:
    #         return True
    #     elif p is None or q is None:
    #         return False
    #     elif p.val!=q.val:
    #         return False
    #     else:
    #         lsub = self.same(p.left, q.right)
    #         rsub = self.same(p.right, q.left)
    #         return lsub and rsub
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # same寫在裡面
        def same(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val!=q.val:
                return False
            else:
                # 鏡像, 也就是左子要=右子且右子=左子
                lsub = same(p.left, q.right)
                rsub = same(p.right, q.left)
                return lsub and rsub
        # 找出root的左右child, recursive下去判斷是否鏡像
        ltree = root.left
        rtree = root.right
        return same(ltree, rtree)

# By BFS(iterative), time: O(n), space: O(n)
# 雖然要同時判斷兩個tree, 但可以只用一個queue做到
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         rtree = root.right
#         ltree = root.left    
#         # 建立queue
#         queue = collections.deque()
#         # 因要一次看兩個tree, 所以將兩tree node包成一個元素append進去, append一次只能一個元素
#         # append進去的(rtree, ltree)就是當下要比較的兩個元素
#         queue.append((rtree, ltree))
#         while queue:
#             # twonode = queue.popleft()
#             # rtree = twonode[0]
#             # ltree = twonode[1]
#             # pop出來一次是(r, l)這樣的格式, 跟上面同樣意思, 注意不要pop兩次
#             # rtree, ltree等同於(rtree, ltree)
#             rtree, ltree = queue.popleft
#             # 兩者都是None代表不會有child, 直接continnue
#             if rtree is None and ltree is None:
#                 continue
#             elif rtree is None or ltree is None:
#                 return False
#             elif rtree.val!=ltree.val:
#                 return False
#             else:
#                 # 下次比較rtree的右子和ltree的左子
#                 queue.append((rtree.right, ltree.left))
#                 # 以及比較rtree的左子和ltree的右子
#                 queue.append((rtree.left, ltree.right))
#         # 跳出while代表queue沒有任何元素, 也就是已經走訪完兩個tree, 必定是True    
#         return True
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
