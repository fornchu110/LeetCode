#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
# 給一個被rotated過的有序數列, 找出最小值
# rotated定義為:將數列想像為cycle, rotate一次就將所有元素往後一次
# 希望能以log(n)完成

# By binary search, time: O(log(n)), space: O(1)
# 要求用log(n)要想到二分搜尋法, 每次只找目前範圍的半邊所有time是log(n)
# 從目前範圍中間的元素和左界和右界比較, 就可以知道目標(最小元素)在左半邊還是右半邊
class Solution:
    def findMin(self, nums: List[int]) -> int:   
        # 將第0個元素和最後個元素作為範圍的index, 注意r不是以len(nums)作為index 
        l, r = 0, len(nums)-1
        # 題目說不會有重複元素, 只要不是只剩一個元素那l都會<r
        # 這是範圍為左閉右開的寫法, 也就是在[l, r)搜尋答案, 二分查找的區間決定寫法, 是精隨
        # l<r代表不考慮l==r的情況了, 畢竟l==r代表搜索的區間剩一個元素, 即是答案
        while(l<r):
            # pivot是目前範圍中間的元素
            # l+(r-l)//2等同於(l+r)//2, 是為了避免l+r時overflow
            # 整數除法會比起right更靠近left
            # Ex: 3個元素, l=0, r=2, mid = 1, array: 012
            # Ex: 4個元素, l=0, r=3, mid = 1, array: 0123
            pivot = l+(r-l)//2
            # pivot小於r代表最小值在左半邊
            if nums[pivot]<nums[r]:
                # 因我們不希望搜尋重複的範圍, 而現在是左閉右開, 所以r = pivot下次不會搜尋目前的r
                r = pivot
            # 否則代表最小值在右半邊
            else:
                # 同上, 左閉右開所以l+1才不會搜尋這次的l
                l = pivot+1
        # 回傳l或r都一樣, 畢竟就是l==r時結束迴圈的
        return nums[l]

# By min(), time: O(n), space: O(1) 
# python的min()和max就只是走訪一次, 實際上沒省下時間
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         return min(nums)
        
# @lc code=end

