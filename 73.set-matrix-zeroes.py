<<<<<<< HEAD
#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
# 給一個mxn的matrix, 如果matrix內有0, 則把該0同row同col的所有元素都轉換成0

# By inplace flag array, time: O(m*n), space: O(1)
# 避免了用額外O(m+n)的空間儲存flag, 而是由第0個row和第0個col來儲存
# 但這樣會更改第0個row和第0個col之元素(但在這邊貌似不影響, 更重要的是可能會漏了將第0row、col的元素轉換成0)
# 所以要先判斷裡面是否存在0並用flag紀錄, 只要存在0代表整row、col都要是0, 最後再將全部重製為0即可
# 想像外圈(第0row、col)和內圈的0本來就是互相影響, 畢竟只要在同row、col有0, 整個都要變0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # any()是判斷條件內是否存在1或True, 只要存在就return1, 不存在就False
        # 判斷第0個col下有沒有為0的元素
        col0flag = any(matrix[i][0]==0 for i in range(m))
        # 判斷第0個row下有沒有為0的元素
        row0flag = any(matrix[0][j]==0 for j in range(n))
        
        # 以matrix[i][0]和matrix[0][j]來記錄第i個row以及第j個col有沒有0存在
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]==0:
                    #這時除了用第0row、col紀錄外, 也等同於先將第0row、col轉換成0了
                    matrix[i][0] = matrix[0][j] = 0
        
        # 重新走訪第0個row、col外的matrix, 將有0的row和col所有元素轉換成0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        # 如果col0flag不為0, 代表第0個col上不同row的所有元素都該變為0
        if col0flag:
            for i in range(m):
                matrix[i][0] = 0
        # 如果row0flag不為0, 代表第0個row上不同col的所有元素都該變為0
        if row0flag:
            for j in range(n):
                matrix[0][j] = 0

# By flag array, time: O(m*n), space: O(m+n)
# 這題要注意的是後來被改變成0的元素不該拿來被判斷為同row同col變0, 如果用一邊走訪一邊查看0的方式就會有問題
# Ex: 走到matrix[3][2]發現是0, 把其上下左右都更改為0, 但走到matrix[3][3]時, 這邊雖然原本是1被更改為0, 仍會觸發判斷讓matrix[3][3]上下左右改為0
# 所以直觀先走訪一次matrix, 將0元素所在的row和col記錄下來
# 再走訪一次matrix, 將與記錄下的row和col同row、col的元素更改為0
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#         # 0也可以用False代替
#         rowflag = [0]*m
#         colflag = [0]*n
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j]==0:
#                     # 0用False的話這邊1就可以改用True
#                     rowflag[i] = 1
#                     colflag[j] = 1
#         for i in range(m):
#             for j in range(n):
#                 if rowflag[i] or colflag[j]:
#                     matrix[i][j] = 0

# @lc code=end

=======
#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
# 給一個mxn的matrix, 如果matrix內有0, 則把該0同row同col的所有元素都轉換成0

# By inplace flag array, time: O(m*n), space: O(1)
# 避免了用額外O(m+n)的空間儲存flag, 而是由第0個row和第0個col來儲存
# 但這樣會更改第0個row和第0個col之元素(但在這邊貌似不影響, 更重要的是可能會漏了將第0row、col的元素轉換成0)
# 所以要先判斷裡面是否存在0並用flag紀錄, 只要存在0代表整row、col都要是0, 最後再將全部重製為0即可
# 想像外圈(第0row、col)和內圈的0本來就是互相影響, 畢竟只要在同row、col有0, 整個都要變0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # any()是判斷條件內是否存在1或True, 只要存在就return1, 不存在就False
        # 判斷第0個col下有沒有為0的元素
        col0flag = any(matrix[i][0]==0 for i in range(m))
        # 判斷第0個row下有沒有為0的元素
        row0flag = any(matrix[0][j]==0 for j in range(n))
        
        # 以matrix[i][0]和matrix[0][j]來記錄第i個row以及第j個col有沒有0存在
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]==0:
                    #這時除了用第0row、col紀錄外, 也等同於先將第0row、col轉換成0了
                    matrix[i][0] = matrix[0][j] = 0
        
        # 重新走訪第0個row、col外的matrix, 將有0的row和col所有元素轉換成0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        # 如果col0flag不為0, 代表第0個col上不同row的所有元素都該變為0
        if col0flag:
            for i in range(m):
                matrix[i][0] = 0
        # 如果row0flag不為0, 代表第0個row上不同col的所有元素都該變為0
        if row0flag:
            for j in range(n):
                matrix[0][j] = 0

# By flag array, time: O(m*n), space: O(m+n)
# 這題要注意的是後來被改變成0的元素不該拿來被判斷為同row同col變0, 如果用一邊走訪一邊查看0的方式就會有問題
# Ex: 走到matrix[3][2]發現是0, 把其上下左右都更改為0, 但走到matrix[3][3]時, 這邊雖然原本是1被更改為0, 仍會觸發判斷讓matrix[3][3]上下左右改為0
# 所以直觀先走訪一次matrix, 將0元素所在的row和col記錄下來
# 再走訪一次matrix, 將與記錄下的row和col同row、col的元素更改為0
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#         # 0也可以用False代替
#         rowflag = [0]*m
#         colflag = [0]*n
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j]==0:
#                     # 0用False的話這邊1就可以改用True
#                     rowflag[i] = 1
#                     colflag[j] = 1
#         for i in range(m):
#             for j in range(n):
#                 if rowflag[i] or colflag[j]:
#                     matrix[i][j] = 0

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
