#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#

# @lc code=start

# �Narr����int�ھڨ�2�i���ܪk��bit 1 ���ƶq���p�Ӥj�Ƨ�

# By bitwise and sorted(), time: O(nlogn), space: O(logn)
# time�Mspace���O�ƧǩҪ�O��
# �ΨC������sint n, n&(n-1)�ӱN��̫�@��1�ܦ�0, �p�G�S��1�F���۵Mn�ܦ�0�j�餤��
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # �s�Uint��bit 1��
        arr_cnt = []
        for i in arr:
            # �קK�ק�arr�ҥH��tmp�����U��int
            tmp = i
            tmpcnt = 0
            while tmp:
                tmpcnt += 1
                # �N�̫�@��bit 1�ܦ�0
                tmp &= (tmp-1)
            arr_cnt.append(tmpcnt)
        # ��zip�P�ɨ��X, *�Ѷ}list, �A�Nzip�^�Ǫ����Х�list����
        res = list(zip(*sorted(zip(arr_cnt, arr))))
        # res�N�O�Ƨǫ᪺arr_cnt�Marr, �ڭ̭n���Oarr
        return (res[1])
    
# By bin(), time: O(nlogn), space: O(logn)
# time�Mspace���O�ƧǩҪ�O��
# �Τ��ت�bin(num).count('1')�ӼƤG�i��᪺1�ƶq�ᰵ�Ƨ�
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

