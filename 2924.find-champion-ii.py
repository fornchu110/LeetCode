# @lc code=start
# 給一整數n代表有n個node和二維陣列edges, edges是由這n個node所組成的DAG之關係圖
# return能走訪所有節點的node也就是冠軍, 如果不存在冠軍return -1
# 注意不能走向所有node就不存在冠軍, 因為沒打過不能比較

# By greedy, time: O(n), space: O(n)
# 反過來思考, edges(u, v)中的v代表被走向, 也就是被打敗過的node
# 所以只要找出沒被打敗過的node, 再確認沒被打敗過的node是否只有一個即可
# 如果只有一個代表他是冠軍, 不只一個代表不存在冠軍
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int: 
        check = [0 for i in range(n)]
        for u, v in edges:
            check[v] = 1
        res = 0
        cnt = 0
        for i in range(n):
            if check[i]==0:
                res = i
                cnt += 1
        if cnt==1:
            return res
        else:
            return -1


# By BFS, time: O(n^2), space: O(n^2)
# 將edges的關係轉換成二維陣列graph, graph[i][j]代表能從i走到j
# 利用graph對所有node都用BFS做走訪, 走訪時用visted記錄當下走訪過的節點
# 如果走訪過的節點數==n代表成功走到所有點, 這就是冠軍
# class Solution:
#     def __init__(self):
#         self.graph = None
#         self.node_cnt = 0
    
#     def bfs(self, node):
#         visited = set()
#         queue = collections.deque()
#         queue.append(node)

#         while queue:
#             tmp = queue.pop()
#             visited.add(tmp)
#             for v in self.graph[tmp]:
#                 if v not in visited:
#                     queue.append(v)
#         if len(visited)==self.node_cnt:
#             return node
#         else:
#             return -1
    
#     def findChampion(self, n: int, edges: List[List[int]]) -> int: 
#         graph = [[] for i in range(n)]
#         for u, v in edges:
#             graph[u].append(v)
#         self.graph = graph
#         self.node_cnt = n
        
#         for i in range(n):
#             res = self.bfs(i)
#             if res!=-1:
#                 return res
#         return -1
    
# @lc code=end
