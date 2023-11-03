<<<<<<< HEAD
#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start

# By counting sort
# 數出現次數紀錄在array中再依照要求順序加入res 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 找出arr1最大的數字
        upper = max(arr1)
        # 要計算arr1內每個元素各出現多少次
        # frequency[i]就是i這個數字出現的次數, 直接以i做index
        # array最少要有最大數字+1個大小, 因為要以最大數字做index
        # Ex:最大2, array要有三個元素才能0, 1, 2
        frequency = [0]*(upper + 1)
        # 走訪arr1每個元素x開始數頻率
        for x in arr1:
            frequency[x] += 1
        
        res = list()
        for x in arr2:
            # list.appen加入單個元素, list.extend一次加入多個
            # 以arr2出現的順序將frequency[x]個x加入res
            res.extend([x]*frequency[x])
            # frequency = 0用來記錄arr2內的元素都被加入res了
            frequency[x] = 0
        # 將所有arr1內出現在arr2的元素都加入res後    
        # 不能重新對arr1做走訪, 必須對frequency走訪
        # 雖然裡面一定有本來就是空的,會浪費時間
        # 但res要求從小到大排序, 而非剩下元素照arr1內的順序排就可以
        for x in range(upper+1):
            # 只要frequency不為0, 代表是arr2以外的元素
            if frequency[x] > 0:
                # 將他們加入res
                res.extend([x] * frequency[x])
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start

# By counting sort
# 數出現次數紀錄在array中再依照要求順序加入res 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 找出arr1最大的數字
        upper = max(arr1)
        # 要計算arr1內每個元素各出現多少次
        # frequency[i]就是i這個數字出現的次數, 直接以i做index
        # array最少要有最大數字+1個大小, 因為要以最大數字做index
        # Ex:最大2, array要有三個元素才能0, 1, 2
        frequency = [0]*(upper + 1)
        # 走訪arr1每個元素x開始數頻率
        for x in arr1:
            frequency[x] += 1
        
        res = list()
        for x in arr2:
            # list.appen加入單個元素, list.extend一次加入多個
            # 以arr2出現的順序將frequency[x]個x加入res
            res.extend([x]*frequency[x])
            # frequency = 0用來記錄arr2內的元素都被加入res了
            frequency[x] = 0
        # 將所有arr1內出現在arr2的元素都加入res後    
        # 不能重新對arr1做走訪, 必須對frequency走訪
        # 雖然裡面一定有本來就是空的,會浪費時間
        # 但res要求從小到大排序, 而非剩下元素照arr1內的順序排就可以
        for x in range(upper+1):
            # 只要frequency不為0, 代表是arr2以外的元素
            if frequency[x] > 0:
                # 將他們加入res
                res.extend([x] * frequency[x])
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
