<<<<<<< HEAD
#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
# 給一整數n, return一長度為n+1的陣列, 內容為0~n在二進位下1的數量
# 看到bitwise馬上要想到/2(>>1)的規律、奇偶的差異、XOR運算的特性

# By DP and bitwise, time: O(n), space: O(1)
# 要用一個陣列res來儲存res[i]的1數量, 但注意一開始只有一個元素0
# 很直觀的知道i之1數量其中一種規律:若i為2的冪次方時, i只會有一個1
# Ex: res[1] = res[2] = res[4] = res[8]...
# 再來發現不只冪次是這個規律
# 當i是偶數時, res[i]=res[i//2], 當i是奇數時, res[i]=res[i//2]+1
# 因此從i=1開始逐一建立res的內容, 每次查找i//2的結果和做出奇偶時的對應即可, 不需要隨著i增加做額外計算
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            # 用i>>1代替i//2
            # 用i&1知道i是否為奇數, 省去if-else
            res.append(res[i>>1]+(i&1))
        return res

# By bitwise(n&n-1), time: O(nlogn), space: O(n)
# 從0~n+1做迴圈, 每輪用i&i-1的方式檢查1的數量
# 注意n&n-1也可以用來判斷是否為2的冪次方, 因為2的冪次方只有一個1
# 也就是說, n&n-1==0即代表n是2的冪次方
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res =  [0]*(n+1)
#         # 這是index做法的迴圈, 也可以用append的方法少做index=0那次
#         for idx, i in enumerate(range(n+1)):
#             cnt = 0
#             # 記住n和(n-1)做&會把最小bit的1消除掉
#             # 全部都消除掉自然就變成0, 跳出迴圈
#             while i!= 0:
#                 i &= i-1
#                 cnt += 1
#             res[idx] = cnt
#             # 比較差的方法, 一位位看是否為1, 然後再右移看左邊那位
#             # while i!=0:
#             #     if i&1:
#             #         cnt += 1
#             #     i >>= 1
#         return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
# 給一整數n, return一長度為n+1的陣列, 內容為0~n在二進位下1的數量
# 看到bitwise馬上要想到/2(>>1)的規律、奇偶的差異、XOR運算的特性

# By DP and bitwise, time: O(n), space: O(1)
# 要用一個陣列res來儲存res[i]的1數量, 但注意一開始只有一個元素0
# 很直觀的知道i之1數量其中一種規律:若i為2的冪次方時, i只會有一個1
# Ex: res[1] = res[2] = res[4] = res[8]...
# 再來發現不只冪次是這個規律
# 當i是偶數時, res[i]=res[i//2], 當i是奇數時, res[i]=res[i//2]+1
# 因此從i=1開始逐一建立res的內容, 每次查找i//2的結果和做出奇偶時的對應即可, 不需要隨著i增加做額外計算
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            # 用i>>1代替i//2
            # 用i&1知道i是否為奇數, 省去if-else
            res.append(res[i>>1]+(i&1))
        return res

# By bitwise(n&n-1), time: O(nlogn), space: O(n)
# 從0~n+1做迴圈, 每輪用i&i-1的方式檢查1的數量
# 注意n&n-1也可以用來判斷是否為2的冪次方, 因為2的冪次方只有一個1
# 也就是說, n&n-1==0即代表n是2的冪次方
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res =  [0]*(n+1)
#         # 這是index做法的迴圈, 也可以用append的方法少做index=0那次
#         for idx, i in enumerate(range(n+1)):
#             cnt = 0
#             # 記住n和(n-1)做&會把最小bit的1消除掉
#             # 全部都消除掉自然就變成0, 跳出迴圈
#             while i!= 0:
#                 i &= i-1
#                 cnt += 1
#             res[idx] = cnt
#             # 比較差的方法, 一位位看是否為1, 然後再右移看左邊那位
#             # while i!=0:
#             #     if i&1:
#             #         cnt += 1
#             #     i >>= 1
#         return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
