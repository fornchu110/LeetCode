<<<<<<< HEAD
#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
# By XOR(^), time: O(n), space: O(1)
# 給定加密過的list, list內每個元素都是原本arr內相鄰兩倆互相xor而成
# 會先給你arr第一個元素, 要求出arr維和
# 利用了XOR的性質1. x^0 = x, 2. x^x = 0以及交換性和結合性
# 可以看出x^y = z的話, x^z = y且z^y = x, 所以依序做XOR即可得出答案
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # 一開始將first放入就不用append了
        res = [first]
        tmp = first
        for i in encoded:
            tmp ^= i
            res.append(tmp)
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
# By XOR(^), time: O(n), space: O(1)
# 給定加密過的list, list內每個元素都是原本arr內相鄰兩倆互相xor而成
# 會先給你arr第一個元素, 要求出arr維和
# 利用了XOR的性質1. x^0 = x, 2. x^x = 0以及交換性和結合性
# 可以看出x^y = z的話, x^z = y且z^y = x, 所以依序做XOR即可得出答案
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # 一開始將first放入就不用append了
        res = [first]
        tmp = first
        for i in encoded:
            tmp ^= i
            res.append(tmp)
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
