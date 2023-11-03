<<<<<<< HEAD
#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start

# 給一張圖的初始node, node內存放與他有關係的node以及node.val, return關係一模一樣但node為全新的新圖
# 想成deep.copy版的, 這題也可以用copy.deepcopy()作但沒意義
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# By DFS, time: O(n), space: O(n)
# 用DFS走訪圖, 走訪過程建立clone node並將對應的關係和node.val初始化
class Solution(object):
    def __init__(self):
        # 用hash儲存看過的node, key是原始node, value是clone後的node
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node
        # 如果是已經走訪的node
        if node in self.visited:
            # 將其clone版return回去
            return self.visited[node]
        # 如果沒走訪過, 就建立新的clone node初始化value
        clone_node = Node(val = node.val)
        # 看過了
        self.visited[node] = clone_node
        # 只要這個node有neighbors
        if node.neighbors:
            # 用列表生成式
            # 對其neighbors繼續DFS遞迴下去並將他們分別return的clone版放進clone的neighbors
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

# By BFS, time: O(n), space: O(n)
# BFS一樣可以做, 但好信DFS比較快
# class Solution(object):
#     def cloneGraph(self, node):
#         """
#         :type node: Node
#         :rtype: Node
#         """
#         if not node:
#             return node

#         visited = {}
#         queue = collections.deque([node])
#         visited[node] = Node(node.val, [])

#         while queue:
#             tmp = queue.popleft()
#             for neighbor in tmp.neighbors:
#                 if neighbor not in visited:
#                     visited[neighbor] = Node(neighbor.val, [])
#                     queue.append(neighbor)
#                 visited[tmp].neighbors.append(visited[neighbor])
#         return visited[node]

# @lc code=end

=======
#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start

# 給一張圖的初始node, node內存放與他有關係的node以及node.val, return關係一模一樣但node為全新的新圖
# 想成deep.copy版的, 這題也可以用copy.deepcopy()作但沒意義
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# By DFS, time: O(n), space: O(n)
# 用DFS走訪圖, 走訪過程建立clone node並將對應的關係和node.val初始化
class Solution(object):
    def __init__(self):
        # 用hash儲存看過的node, key是原始node, value是clone後的node
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node
        # 如果是已經走訪的node
        if node in self.visited:
            # 將其clone版return回去
            return self.visited[node]
        # 如果沒走訪過, 就建立新的clone node初始化value
        clone_node = Node(val = node.val)
        # 看過了
        self.visited[node] = clone_node
        # 只要這個node有neighbors
        if node.neighbors:
            # 用列表生成式
            # 對其neighbors繼續DFS遞迴下去並將他們分別return的clone版放進clone的neighbors
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

# By BFS, time: O(n), space: O(n)
# BFS一樣可以做, 但好信DFS比較快
# class Solution(object):
#     def cloneGraph(self, node):
#         """
#         :type node: Node
#         :rtype: Node
#         """
#         if not node:
#             return node

#         visited = {}
#         queue = collections.deque([node])
#         visited[node] = Node(node.val, [])

#         while queue:
#             tmp = queue.popleft()
#             for neighbor in tmp.neighbors:
#                 if neighbor not in visited:
#                     visited[neighbor] = Node(neighbor.val, [])
#                     queue.append(neighbor)
#                 visited[tmp].neighbors.append(visited[neighbor])
#         return visited[node]

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
