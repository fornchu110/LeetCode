<<<<<<< HEAD
#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
# 給一已排序陣列nums和target, 找出target在nums中第一次出現和最後一次出現的index

# By binary search: time: O(logn), space: O(1)
# 看到排序和找就要想到binary search
# 自己實作二分搜尋, 根據需求改變內容
class Solution:
    # 第一種寫法, [l, r), 好理解而且return l或r都可以, 推薦
    def binarySearch1(self, nums, target):
        l = 0
        r = len(nums)
        # 左閉右開寫法, 最保險
        while(l<r):
            # (l+r)//2避免overflow的作法
            mid = (r-l)//2+l
            # nums[mid]<target時要往左看, 由於//2會取整往左取且l是閉區間所以縮小範圍要+1
            # nums[mid]>=target時只有r在動了縮小範圍, 最後會在l==r中止
            if nums[mid]<target:
                l = mid+1
            # 因為r是開區間必定能夠縮小範圍
            else:
                r = mid
        # 左閉右開寫法return r也可以
        return l
    # 第二種寫法, [l, r]
    def binarySearch2(self, nums, target):
        l = 0
        # r是閉須間
        r = len(nums)-1
        # 左閉右閉寫法
        while(l<=r):
            mid = (r-l)//2+l
            # 一樣l在不動後處理nums[mid]>=target, 直到r<l才會停止迴圈
            if nums[mid]<target:
                l = mid+1
            else:
                # r是閉區間所以縮小r範圍必須-1, 不然會無窮迴圈
                r = mid-1
        # 在找到target前l先停在target的位置了, 中止時r<l所以r的話return r+1才可以
        return l
    
    # 第三種寫法, (l, r)
    def binarySearch3(self, nums, target):
        l = -1
        r = len(nums)
        # 開區間寫法, 想成在整數情況下(l, r)= [l+1, r-1]
        while(l+1<=r-1):
            mid = (r-l)//2+l
            if nums[mid]<target:
                # 開區間必定不會再看到mid
                l = mid
            else:
                # 一樣開區間
                r = mid
        # return r或是l+1都可以
        return r
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx1 = self.binarySearch1(nums, target)
        if(idx1==len(nums) or nums[idx1]!=target):
            return [-1, -1]
        # 因為找到target最右邊的index等同找到比target大1的數最左邊的index-1
        # 二分搜尋沒有寫nums[mid]==target才return, 所以target+1不存在也沒關係
        idx2 = self.binarySearch1(nums, target+1)-1
        return [idx1, idx2]
    
# By binary search(bisect.bisect()), time: O(logn), space: O(1)
# Python用bisect模組的作法
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         # 注意bisec回傳的是插入點, 也就是說bisect會照排序return加入一個新的target進nums後他的index, 只是加入最左還是最右
#         # Ex: [1, 2, 3]、t = 2, bisect_left(nums) = 1, 因為會變成[1, 2, 2, 3], bisect_right = 2
#         # 所以在bisect_left得到的結果並無差別, 但bisect_right要-1
#         r = bisect_right(nums, target)-1
#         l = bisect_left(nums, target)
#         # l跟r要在nums長度範圍內, 且nums[r]和nums[l]的確是查找的target
#         if l<=r and r<len(nums) and nums[r]==target and nums[l]==target:
#             return [l, r]
#         # 否則代表找不到, 也就是[-1, -1]
#         else:
#             return [-1, -1] 

        
# @lc code=end

=======
#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
# 給一已排序陣列nums和target, 找出target在nums中第一次出現和最後一次出現的index

# By binary search: time: O(logn), space: O(1)
# 看到排序和找就要想到binary search
# 自己實作二分搜尋, 根據需求改變內容
class Solution:
    # 第一種寫法, [l, r), 好理解而且return l或r都可以, 推薦
    def binarySearch1(self, nums, target):
        l = 0
        r = len(nums)
        # 左閉右開寫法, 最保險
        while(l<r):
            # (l+r)//2避免overflow的作法
            mid = (r-l)//2+l
            # nums[mid]<target時要往左看, 由於//2會取整往左取且l是閉區間所以縮小範圍要+1
            # nums[mid]>=target時只有r在動了縮小範圍, 最後會在l==r中止
            if nums[mid]<target:
                l = mid+1
            # 因為r是開區間必定能夠縮小範圍
            else:
                r = mid
        # 左閉右開寫法return r也可以
        return l
    # 第二種寫法, [l, r]
    def binarySearch2(self, nums, target):
        l = 0
        # r是閉須間
        r = len(nums)-1
        # 左閉右閉寫法
        while(l<=r):
            mid = (r-l)//2+l
            # 一樣l在不動後處理nums[mid]>=target, 直到r<l才會停止迴圈
            if nums[mid]<target:
                l = mid+1
            else:
                # r是閉區間所以縮小r範圍必須-1, 不然會無窮迴圈
                r = mid-1
        # 在找到target前l先停在target的位置了, 中止時r<l所以r的話return r+1才可以
        return l
    
    # 第三種寫法, (l, r)
    def binarySearch3(self, nums, target):
        l = -1
        r = len(nums)
        # 開區間寫法, 想成在整數情況下(l, r)= [l+1, r-1]
        while(l+1<=r-1):
            mid = (r-l)//2+l
            if nums[mid]<target:
                # 開區間必定不會再看到mid
                l = mid
            else:
                # 一樣開區間
                r = mid
        # return r或是l+1都可以
        return r
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx1 = self.binarySearch1(nums, target)
        if(idx1==len(nums) or nums[idx1]!=target):
            return [-1, -1]
        # 因為找到target最右邊的index等同找到比target大1的數最左邊的index-1
        # 二分搜尋沒有寫nums[mid]==target才return, 所以target+1不存在也沒關係
        idx2 = self.binarySearch1(nums, target+1)-1
        return [idx1, idx2]
    
# By binary search(bisect.bisect()), time: O(logn), space: O(1)
# Python用bisect模組的作法
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         # 注意bisec回傳的是插入點, 也就是說bisect會照排序return加入一個新的target進nums後他的index, 只是加入最左還是最右
#         # Ex: [1, 2, 3]、t = 2, bisect_left(nums) = 1, 因為會變成[1, 2, 2, 3], bisect_right = 2
#         # 所以在bisect_left得到的結果並無差別, 但bisect_right要-1
#         r = bisect_right(nums, target)-1
#         l = bisect_left(nums, target)
#         # l跟r要在nums長度範圍內, 且nums[r]和nums[l]的確是查找的target
#         if l<=r and r<len(nums) and nums[r]==target and nums[l]==target:
#             return [l, r]
#         # 否則代表找不到, 也就是[-1, -1]
#         else:
#             return [-1, -1] 

        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
