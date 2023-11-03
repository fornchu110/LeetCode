#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
# 給一二維陣列matrix, 要求將matrix做inplace順時鐘旋轉90度, 所以不能return

# By inplace modification, time: O(n^2), space: O(1)
# 完全不使用額外的空間(輔助矩陣)來記錄, 直接做inplace調整
# 將一個元素旋轉90會到對應位置, 旋轉180、270又到兩個對應位置, 旋轉360則回到原位
# 所以實際上無論對matrix內任何元素, 都是在做其與90、180、270這三位置上之元素的變更
# Ex 四角是1、3、9、7, 順時鐘轉90變成7、1、3、9
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 每4個元素會是一組, 所以大概會做n^2/4, 也就是(n/2)*(n/2)次
        # 一般整數除法往下取
        for i in range(n//2):
            # n+1代表做整數除法時往上取, 只在n是奇數時有差
            # 會需要做是因為奇數x奇數方陣時, 中間的元素不會變
            # Ex: 5x5矩陣中間不會變, 要討論左上以及相對應順時鐘轉90、180、270的2x3矩陣
            for j in range((n+1)//2):
                # 會注意到inplace更改4個元素總會遺失一個元素的值
                # 所以用tmp將當下的元素存下來, 類似做a和b值交換時要先用個tmp暫存
                tmp = matrix[i][j]
                # 轉90度第i列會變i行, 而第n-1-j行會變j列
                matrix[i][j] = matrix[n-1-j][i]
                # 原本的n-1-i行會變成n-1-(n-1-i) = i列
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp

# By record matrix by deepcopy, time: O(n^2), space: O(n^2)
# inplace修改的過程會喪失原本matrix的元素
# 雖然要求matrix本身要inplace, 但沒限定無法用額外的空間來記錄matrix內容
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix)
#         # 想像python都是指標變數, 所以在a是陣列時, 單純用b = a會在更動a的同時更動b
#         # copy.copy是淺複製, 一般來說更動a不會再更動b, 但若更動到a內b有參考的變數(例如第二維的list)仍會影響
#         # 而copy.deepcopy是將對象參數完全複製一份到新的變數下, 所以兩者完全獨立不會影響
#         # 這邊對象參數是matrix, 所以tmp也是一個二維陣列
#         tmp = copy.deepcopy(matrix)
#         # 走訪tmp將matrix值變更
#         for i in range(n):
#             for j in range(n):
#                 # 順時鐘旋轉90度公式經過觀察可得
#                 # 第i行會到第n-1-i列, 第j列會到第j行
#                 matrix[j][n-1-i] = tmp[i][j]
        
# @lc code=end

