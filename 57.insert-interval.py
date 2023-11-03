#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
# 給一堆閉區間的intervals和一個新區間newInterval
# 只要intervals內和newInterval重疊的區間就將他們合併, 合併後的下界就是這些區間最小下屆, 上屆就是這些區間最大上屆
# return不重疊的區間和合併區間, 這些區間要由小到大排序

# By simulation, time: O(n), space: O(1)
# 重點在於如何判斷各個區間是否有和newInterval重疊
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # mer代表合併區間
        mer = newInterval
        # 用flag來判斷什麼時候要將tmp加入res
        flag = 1
        for i in intervals:
            # i[0]代表區間下界, i[1]代表區間上界, 下界必定<=上界
            # 當走訪到的i之下界比newInterval的上界還高, 代表不可能與newInterval重疊
            # 且這個i之後的下界肯定也更高不可能重疊, 因此可以將mer加入res
            # 避免nerInterval上界本來就比多個i的下界還低造成重複加入, 所以需要flag
            if flag and i[0]>newInterval[1]:
                res.append(mer)
                # 將mer加入res了, 不會再需要加入其他次
                flag = 0
            # 重點在此, 只有兩種情況區間不和newInterval重疊
            # 1. 區間的上界比newIterval下界還小
            # 2.區間的下界比newInterval上界還大
            if i[1]<min(newInterval) or i[0]>max(newInterval):
                res.append(i)
            # 其他情況都代表區間和newInterval有重疊
            # 那就來看是否要更新mer的上下界
            # 重疊的話新下界就是重疊區間中下界最小的下界, 新上界就是重疊區間中上界最大的上界
            # 這邊不用看, 但如果是要看重疊的交集, 那交集下界就是重疊區間中最大的下界, 上界就是重疊區間中最小的上界
            else:
                if i[0]<mer[0]:
                    mer[0] = i[0]
                if i[1]>mer[1]:
                    mer[1] = i[1]
        # flag為1代表走訪完interval仍沒將mer加入res, 所以補上
        if flag:
            res.append(mer)
        # res要照區間大小排序, 但下面這樣做要花額外時間排序不好
        # res.append(tmp)
        # res.sort()
        return res
        
# @lc code=end

