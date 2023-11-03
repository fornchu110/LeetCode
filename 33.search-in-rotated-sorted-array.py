#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
# 給一個rotated過的有序數列, 要求找出target是否在數列中, 在的話return index否則-1
# 規定要在time: O(log(n))解決, 想到二分搜尋

# By binary search, time: O(log(n)), space: O(1)
# 二分搜尋法, 這題一樣可以用[l, r)左閉右開的區間做
# 這題的想法是, 先看mid左邊和右邊哪邊是單調有序, 再看target是否位於單調那邊來決定區間
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # not nums用來判斷nums是否為空, 也就是[], 但題目說至少有一個元素所以不需要
        # if not nums:
        #     return -1
        l, r = 0, len(nums)-1
        # while條件就是使用的搜尋區間, 我選擇[l, r)左閉右開區間
        while l<r:
            mid = l+(r-l)//2
            # 當mid==target直接返回
            if nums[mid]==target:
                return mid
            # 若mid比nums[len(nums)-1]還小, 代表右邊是單調有序
            if nums[mid]<nums[len(nums)-1]:
                # 右邊是單調有序所以能直接判斷target是否在右邊
                # 注意target不可能==nums[mid], 否則前面已經return
                if nums[mid]<target<=nums[len(nums)-1]:
                    # target在右邊那縮小範圍把l設定為mid+1
                    l = mid+1
                # target在左邊, 而看的是[l, r)所以r = mid
                else:
                    r = mid
            # 若mid>=nums[len(nums)-1], 代表左邊是單調有序
            else:
                # 直接判斷target是否位於左邊
                # 一樣注意target不可能==nums[mid]
                if nums[0]<=target<nums[mid]:
                    # 位於左邊, 縮小範圍把r設定成mid
                    r = mid
                # 位於右邊, 縮小l的範圍
                else:
                    l = mid+1
        # 因我是用while l<r, 所以當l==r也就是範圍內剩下一個元素時會跳出
        # 要判斷剩下的這個元素是否==target, 用nums[l]和nums[r]都一樣
        if nums[l]==target:
            return l
        return -1
        
# @lc code=end

