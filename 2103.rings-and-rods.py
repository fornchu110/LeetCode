<<<<<<< HEAD
#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
# 給一串rings上面每兩個寫放什麼顏色的ring在幾號rod
# 最後return有幾個rod上面有R、G、B三種ring

# By bitwise, time: O(n+k), space: O(k)
# 仍然是index array, 但不需要三個array, 一個array對內容元素做bitwise操作即可
# Ex: 二進位111代表R、G、B都有, 101代表沒有G, 001代表只有R
class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        # 紀錄各個rod有哪些顏色ring的index array
        status = [0] * 10   
        for i in range(0, n, 2):
            # python的int()會自動把字元轉成int而非ascii, 所以也不能直接對字元做運算
            idx = int(rings[i+1])
            # 不用3三個array的原因, 用2進位的個位數紀錄
            # R在第0位, G在第1位, B在第2位
            if rings[i] == 'R':
                status[idx] |= 1
            elif rings[i] == 'G':
                status[idx] |= 2
            else:
                status[idx] |= 4
        res = 0
        for i in status:
            # 二進位111等同於十進位7
            if i == 7:
                res += 1
        return res

# By index array and ord(), time: O(n+k), space: O(3*k), n = len(rings), k = rod數量   
# 用index array的方式記錄各顏色ring放在哪個rod, 最後看那些index同時在三array上為1
# class Solution:
#     def countPoints(self, rings: str) -> int:
#         res = 0
#         r = [0]*10
#         g = [0]*10
#         b = [0]*10
#         n = len(rings)
#         for i in range(1, n, 2):
#             if rings[i-1]=='R':
#                 r[ord(rings[i])-ord('0')] += 1
#             if rings[i-1]=='G':
#                 g[ord(rings[i])-ord('0')] += 1
#             if rings[i-1]=='B':
#                 b[ord(rings[i])-ord('0')] += 1
#         for i, j , k in zip(r, g ,b):
#             if i!=0 and j!=0 and k!=0:
#                 res += 1
#         return res

# @lc code=end

=======
#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
# 給一串rings上面每兩個寫放什麼顏色的ring在幾號rod
# 最後return有幾個rod上面有R、G、B三種ring

# By bitwise, time: O(n+k), space: O(k)
# 仍然是index array, 但不需要三個array, 一個array對內容元素做bitwise操作即可
# Ex: 二進位111代表R、G、B都有, 101代表沒有G, 001代表只有R
class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        # 紀錄各個rod有哪些顏色ring的index array
        status = [0] * 10   
        for i in range(0, n, 2):
            # python的int()會自動把字元轉成int而非ascii, 所以也不能直接對字元做運算
            idx = int(rings[i+1])
            # 不用3三個array的原因, 用2進位的個位數紀錄
            # R在第0位, G在第1位, B在第2位
            if rings[i] == 'R':
                status[idx] |= 1
            elif rings[i] == 'G':
                status[idx] |= 2
            else:
                status[idx] |= 4
        res = 0
        for i in status:
            # 二進位111等同於十進位7
            if i == 7:
                res += 1
        return res

# By index array and ord(), time: O(n+k), space: O(3*k), n = len(rings), k = rod數量   
# 用index array的方式記錄各顏色ring放在哪個rod, 最後看那些index同時在三array上為1
# class Solution:
#     def countPoints(self, rings: str) -> int:
#         res = 0
#         r = [0]*10
#         g = [0]*10
#         b = [0]*10
#         n = len(rings)
#         for i in range(1, n, 2):
#             if rings[i-1]=='R':
#                 r[ord(rings[i])-ord('0')] += 1
#             if rings[i-1]=='G':
#                 g[ord(rings[i])-ord('0')] += 1
#             if rings[i-1]=='B':
#                 b[ord(rings[i])-ord('0')] += 1
#         for i, j , k in zip(r, g ,b):
#             if i!=0 and j!=0 and k!=0:
#                 res += 1
#         return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
