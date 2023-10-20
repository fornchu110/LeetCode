#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
# 給一陣列nums, 可以做nums[i]-1同時nums[i-1]+1的操作, 想辦法讓max(nums)變最小並return這個值

# By, category discussion, time: O(n), space: O(1)
# 分類討論法, 有點像dp的概念, 做法又有點像prefix
# 利用這題的操作實際上是將nums內元素盡可能的平均化這點, 只要後面的元素夠大就能一直做平均
# 觀察後發現甚麼叫做夠大?實際上就是比前面所有元素的平均值還大
# 一開始只有一個元素時, 最大值就是一個元素
# 每走到新的元素, 如果新元素比上次算出的最大值還大, 代表可以做平均(因後面的可以分給前面)
# 把到新元素為止的元素加總並平均化, 就是新的最大值
# 如果新元素比之前算出的最大值還小, 代表最大值不變
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = []
        # enumerate起始值為1, 是為了知道目前有幾個元素, accululate是每走到新元素的元素和
        # Ex, nums = [1, 2, 3, 4], accumulate(nums) = [1, 3, 6, 10]
        for num, i in enumerate(accumulate(nums), 1):
            # 由於規定元素都是int, 所以多餘的平均值不能捨棄
            # 平均值是3.5那max就要是4, 因此必須向上取整
            # +(num-1)是向上取整的技巧, 做法是加上分母後-1, -1是為了避免整除
            # Ex: 12//5向上取整 = (12+5)//5 = 3
            # 但15//5我們一樣希望是向上取整時, (15+5)//5 = 4, 不符合15//5向上取整 = 3的結果
            # 所以(15+5-1)//5 = (15+4)//5避免了多加1, 且不會對不整除的情況影響
            # 分母是1時本來就沒有向上取整向下取整的問題, 所以+1再-1沒差
            res.append((i+(num-1))//num)
        # 因為這裡的作法是無論如何算出當下所有元素的平均, 所以要找max
        return max(res)
        # 列表生成式寫法, 會比append更快一點
        return max((i+(num-1))//num for num, i in enumerate(accumulate(nums), 1))
    
# By binary solution, time: O(nlogm), space: O(1), m = max(nums)
# 二分答案法
# 注意min(max)和max(min), 也就是最小化最大值或最大化最小值的問題, 都可以用二分答案法來做
# 雖然一次只能同時操作nums[i]和nums[i-1], 但注意這並不代表只有nums[i]的數能給nums[i-1]
# Ex: [7, 8, 8, 9], 因為並沒限定操作次數, 所以只要將9的1一直往前移變成[8, 8, 8, 8]即可
# 利用二分查找縮小新max(nums)也就是res的區間
# Ex: [2, 3, 7], 這個陣列最後變成[4, 4, 4], 實際上是將7的2個1分給2和1個1分給3變成的
# 可以觀察到基本上是在符合條件下將nums更加平均化
# class Solution:   
#     def minimizeArrayValue(self, nums: List[int]) -> int:
#         # check目的是給res為max時, 檢測是否可行, 模擬確認的過程
#         # Ex: 給陣列[3, 5], 若res為4, 那走到3時會剩下1個coda讓後面比4大的數變小
#         # 給陣列[5, 3], 若res為4, 會發現因為前面不能給後面, 所以4直接不可行, 會return False
#         def check(nums, res):
#             # 扣打一開始是0, 因只有遇到比res更小的數才有餘力將後面的數變小
#             coda = 0
#             # 從頭走訪確認新的res能否成立
#             for i in nums:
#                 if i<=res:
#                     coda += res-i
#                 else:
#                     if coda<i-res:
#                         return False
#                     else:
#                         coda -= (i-res)
#             return True
        
#         # 注意使用二分查找並不是為了走訪陣列, 所以left和right並不是index
#         # left和max代表的是新res所在的區間, 當結束代表新res只剩一種可能, 也就是最佳解
#         # 為何能保證最佳?因為這實際上是在res不符合條件時才增加res, res符合條件時盡量減少res
#         left = 0
#         right = max(nums)
#         # 新max(nums)必定在[0, max(nums)]區間, 利用二分查找找出新max(nums)更有效率
#         # 二分查找的過程就是變更res並測試的過程, 二分的目的在於從max(nums)//2開始找是O(logn)
#         # 比從0往上或從max(nums)往下開始找的O(n)更好
#         while left<right:
#             # mid實際上就是此輪假設的新max(nums), 也就是res
#             mid = (right-left)//2+left
#             # check為True代表以目前mid作為res可行, 那下次讓mid更小試試
#             if check(nums, mid):
#                 right = mid
#             # check為False代表目前mid作為res不可行, 也就是太小, 那下次讓mid更大
#             else:
#                 left = mid+1
#         # 當二分查找結束代表找出了可行的最小max(nums)
#         return left
    
# 上面這個二分答案, python能做的短寫法
# class Solution:
#     def minimizeArrayValue(self, nums: List[int]) -> int:
#         def check(limit: int) -> bool:
#             extra = 0
#             for i in range(len(nums) - 1, 0, -1):
#                 extra = max(nums[i] + extra - limit, 0)
#             return nums[0] + extra <= limit
#         return bisect_left(range(max(nums)), True, key=check)

# @lc code=end

