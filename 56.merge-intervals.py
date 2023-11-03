<<<<<<< HEAD
#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
# 給陣列intervals內放多個未排序過的區間, 如果裡面有重疊的區間就將其合併, return處理完的結果

# By one by one compare, time: O(nlogn), space: O(logn)
# space = O(logn)原因是排序所花費的空間複雜度
# 想走訪一次就結束必定要先排序過, 花費O(nlogn)

# 更好的做法應該是對res的元素做修改和比較, 少判斷第二個邊界條件
# 因會先以下界sort過所以實際上只要看以及更改上界
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # key = lamada這個參數是sort()中省下排序實際時間重要的技巧
        # 以這邊為例, 我只想讓區間根據下界做排序
        # 因此key = lambda x代表裡面這些區間都是x
        # 而x[0]就是下界, 這樣就成功指定以下界排序, 而不對拿出處理上界的元素
        # 如果是對list內的多個dict做排序, key就可以指定只判斷那項key之value做排序, 而不用看其他的
        # 而且還可以選擇以多個key做判斷只是不同優先度, 這邊如果加入上界作為條件
        # 就要寫成: key = lambda x: x[0], x[1]
        # 同時可以做到動態計算條件, 像我如果想以上界-下界的值來排序區間
        # 那就寫成: key = lamda x: x[1]-x[0]
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            # res是空或目前區間的下界比res最後一個區間的上界大, 直接將區間加入res
            # res[-1]是存取最後一個元素的技巧
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

# 這邊我做的
# 想法從第一個元素是走訪intervals一一比較並修改intervals做相對應的動作
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         res = []
#         intervals.sort(key = lambda x: x[0])
#         # 邊界條件, 當只有一個區間就可以直接return
#         if len(intervals)==1:
#             return intervals
#         for i in range(1, len(intervals)):
#             # 如果跟上個區間沒有重疊, 則把上個區間加入res
#             # 注意沒區間沒重疊的判定方法:下界>他的上界或上界<他的下界, 除此外都有重疊
#             if intervals[i][0]>intervals[i-1][1] or intervals[i][1]<intervals[i-1][0]:
#                 res.append(intervals[i-1])
#             # 如果跟上個區間有重疊, 則把intervals內現在的區間的上下界改成重疊後的區間
#             else:
#                 intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
#                 intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
#             # 邊界條件, 當走訪到最後一個區間時
#             # 如果是沒重疊情況, 除了把上個區間加入res外也要將自身加入res
#             # 如果是重疊情況, 在更改完自身區間上下界後也要將自身加入res
#             if i==len(intervals)-1:
#                 res.append(intervals[i])
#         return res

# @lc code=end

=======
#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
# 給陣列intervals內放多個未排序過的區間, 如果裡面有重疊的區間就將其合併, return處理完的結果

# By one by one compare, time: O(nlogn), space: O(logn)
# space = O(logn)原因是排序所花費的空間複雜度
# 想走訪一次就結束必定要先排序過, 花費O(nlogn)

# 更好的做法應該是對res的元素做修改和比較, 少判斷第二個邊界條件
# 因會先以下界sort過所以實際上只要看以及更改上界
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # key = lamada這個參數是sort()中省下排序實際時間重要的技巧
        # 以這邊為例, 我只想讓區間根據下界做排序
        # 因此key = lambda x代表裡面這些區間都是x
        # 而x[0]就是下界, 這樣就成功指定以下界排序, 而不對拿出處理上界的元素
        # 如果是對list內的多個dict做排序, key就可以指定只判斷那項key之value做排序, 而不用看其他的
        # 而且還可以選擇以多個key做判斷只是不同優先度, 這邊如果加入上界作為條件
        # 就要寫成: key = lambda x: x[0], x[1]
        # 同時可以做到動態計算條件, 像我如果想以上界-下界的值來排序區間
        # 那就寫成: key = lamda x: x[1]-x[0]
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            # res是空或目前區間的下界比res最後一個區間的上界大, 直接將區間加入res
            # res[-1]是存取最後一個元素的技巧
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

# 這邊我做的
# 想法從第一個元素是走訪intervals一一比較並修改intervals做相對應的動作
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         res = []
#         intervals.sort(key = lambda x: x[0])
#         # 邊界條件, 當只有一個區間就可以直接return
#         if len(intervals)==1:
#             return intervals
#         for i in range(1, len(intervals)):
#             # 如果跟上個區間沒有重疊, 則把上個區間加入res
#             # 注意沒區間沒重疊的判定方法:下界>他的上界或上界<他的下界, 除此外都有重疊
#             if intervals[i][0]>intervals[i-1][1] or intervals[i][1]<intervals[i-1][0]:
#                 res.append(intervals[i-1])
#             # 如果跟上個區間有重疊, 則把intervals內現在的區間的上下界改成重疊後的區間
#             else:
#                 intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
#                 intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
#             # 邊界條件, 當走訪到最後一個區間時
#             # 如果是沒重疊情況, 除了把上個區間加入res外也要將自身加入res
#             # 如果是重疊情況, 在更改完自身區間上下界後也要將自身加入res
#             if i==len(intervals)-1:
#                 res.append(intervals[i])
#         return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
