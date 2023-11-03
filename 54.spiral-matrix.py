#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
# 給一m*n的二維陣列, 要求照著左上->右上->右下->左下->左上這樣螺旋的順序走訪, return走訪時的元素值

# By simulation recursive, time: O(m*n), space: O(1), res不算空間
# 一樣是將整個matrix走訪一次
# 想辦法走訪最外圈, 下一次就把最外圈拿掉再想辦法走訪最外圈...
# 麻煩點再於最後一輪時, 已經不是一個可以繞圈的矩陣, 不一行就是一列
# 實際上會比一般模擬快, 這題也可以寫成子函式做recursive, 但這種想法這邊用for loop也做得到
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        # 再剩下最後一層前, 會循環min(m, n)//2次重複走訪外圈
        for turn in range(min(m, n)//2):
            for i in range(turn, n-turn):
                res.append(matrix[turn][i])
            for i in range(turn+1, m-turn):
                res.append(matrix[i][n-turn-1])
            for i in range(n-turn-2, turn-1, -1):
                res.append(matrix[m-turn-1][i])
            for i in range(m-turn-2, turn, -1):
                res.append(matrix[i][turn])

        if min(m, n)%2 == 1:
            # 先會循環min(m, n)//2次
            turn = min(m, n)//2
            # 再來根據m和n哪個大決定最後一次是走一個row還是一個col
            # 若m<n代表col比較多, 會剩下一個row, 而m=n就是剩下一個元素
            if m<=n:
                # 走訪row時row值固定col變化
                for i in range(turn, n-turn):
                    res.append(matrix[turn][i])
            # m>n同理, 剩下一個col
            else:
                # 走訪col, col值固定row變化
                for i in range(turn, m-turn):
                    res.append(matrix[i][n-turn-1])
        return res
    
# 官方另外對這個方法的寫法
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return list()
        
#         rows, columns = len(matrix), len(matrix[0])
#         order = list()
#         left, right, top, bottom = 0, columns - 1, 0, rows - 1
#         while left <= right and top <= bottom:
#             for column in range(left, right + 1):
#                 order.append(matrix[top][column])
#             for row in range(top + 1, bottom + 1):
#                 order.append(matrix[row][right])
#             if left < right and top < bottom:
#                 for column in range(right - 1, left, -1):
#                     order.append(matrix[bottom][column])
#                 for row in range(bottom, top, -1):
#                     order.append(matrix[row][left])
#             left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
#         return order

# By simulation, time: O(m*n), space: O(m*n)
# 優化空間複雜度的方式是用更改走訪過的元素時, 這題元素在-100~100間, 所以只要走訪後加上201, 再判斷是否>200即可知道是否走訪過
# 這樣做的話space就是O(1)
# 走訪順序是右->下->左->上->右, 遇到底時會更改走訪順序
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return list() 
#         rows, columns = len(matrix), len(matrix[0])
#         # 用visited來儲存那些元素被走訪過
#         visited = [[False]*columns for i in range(rows)]
#         total = rows*columns
#         order = [0]*total
#         # 代表右 下 左 上四種走訪模式
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         row, column = 0, 0
#         directionIndex = 0
#         for i in range(total):
#             order[i] = matrix[row][column]
#             visited[row][column] = True
#             nextRow, nextColumn = row+directions[directionIndex][0], column+directions[directionIndex][1]
#             if not (0 <= nextRow<rows and 0<=nextColumn<columns and not visited[nextRow][nextColumn]):
#                 directionIndex = (directionIndex + 1)%4
#             row += directions[directionIndex][0]
#             column += directions[directionIndex][1]
#         return order

