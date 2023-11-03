#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#

# @lc code=start

# 將arr內的int根據其2進位表示法的bit 1 的數量做小而大排序

# By bitwise and sorted(), time: O(nlogn), space: O(logn)
# time和space都是排序所花費的
# 用每次走到新int n, n&(n-1)來將其最後一位1變成0, 如果沒有1了那自然n變成0迴圈中止
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # 存各int的bit 1數
        arr_cnt = []
        for i in arr:
            # 避免修改arr所以用tmp獲取當下的int
            tmp = i
            tmpcnt = 0
            while tmp:
                tmpcnt += 1
                # 將最後一位bit 1變成0
                tmp &= (tmp-1)
            arr_cnt.append(tmpcnt)
        # 用zip同時走訪, *解開list, 再將zip回傳的指標用list接受
        res = list(zip(*sorted(zip(arr_cnt, arr))))
        # res就是排序後的arr_cnt和arr, 我們要的是arr
        return (res[1])
    
# By bin(), time: O(nlogn), space: O(logn)
# time和space都是排序所花費的
# 用內建的bin(num).count('1')來數二進位後的1數量後做排序
# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         # Define a custom comparison key function for sorting
#         def custom_sort_key(num):
#             # Calculate the number of set bits (1s) in the binary representation of num
#             bit_count = bin(num).count('1')
#             return (bit_count, num)

#         # Sort the input list using the custom comparison key function
#         arr.sort(key=custom_sort_key)

#         # Return the sorted list
#         return arr
# @lc code=end

