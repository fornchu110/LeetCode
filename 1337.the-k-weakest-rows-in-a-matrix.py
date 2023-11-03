#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
# 給一個二維陣列mat和整數k, 每一列根據1的數量決定強弱, 最後要return前k小之列的index
# 兩列1數量向同的話, index較小者較弱
# 1總是在0的左邊

# By binary search and heap, time: O(mlogn+klogm), space: O(m), 其中m是行數、n是列數, 而space是heap在排序過程之消耗
# 這題因為1總在0的左邊, 可以用二分查找來看1的位置得知1的數量, 而不是走訪全部mat
# 要將hash排序的題目或許改成打包tuple用heap更好? 因為heap不做排序而是在建立時決定位置
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            # l, r, pos = 0, n-1, -1
            # while l <= r:
            #     mid = (l + r) // 2
            #     if mat[i][mid] == 0:
            #         r = mid - 1
            #     else:
            #         pos = mid
            #         l = mid + 1
            # 用bisect達到上面效果, bisect_left代表遇到相同元素時找左邊的 
            # bisect_left()的參數要是排序好的list
            # 將mat中每一列用[::-1]反轉後達到由右向左找1的效果
            # 而n-這個index-1才是未反轉時的index
            pos = n-bisect_left(mat[i][::-1], 1)-1
            # 1的個數是最後一個1所在index+1
            # 將1的數量和列之index包成tuple放入power(list)
            power.append((pos+1, i))
        # 將power這個list轉換成heap, 這個heap是min heap, 所以1數量最小的會被放在上面
        # 記住這個語法, 跟collections.deque()類似
        heapq.heapify(power)
        res = list()
        for i in range(k):
            # 將k個列之index pop出來
            res.append(heapq.heappop(power)[1])
        return res

# By hash and sorted, time: O(n^2), space: O(logn)
# 先走訪一次mat建立好每列1數量之hash, 再將hash根據value(也就是1的數量)做排列
# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         hash = {}
#         for i in range(len(mat)):
#             tmp = 0
#             for j in range(len(mat[0])):
#                 if mat[i][j]==1:
#                     tmp += 1
#             hash[i] = tmp
#         # 重點, dict只能用sorted返還成一個list, 沒有dict.sort
#         # 返還成list後就沒有dict的功能, 而是將key和value包成一個tuple
#         # 第一個參數設定將hash內所有元素作排列, key就是x[1]也就是value
#         sortedhash = sorted(hash.items(), key = lambda x:x[1])
#         print(sortedhash)
#         res = []
#         # 將前i個hash的key加入答案
#         for i in range(k):
#             # [0]是key, [1]是value
#             res.append(sortedhash[i][0])
#         return res
        
        
# @lc code=end

