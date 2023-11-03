<<<<<<< HEAD
#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
# 給兩字串s和t, 如果s和t的字元一模一樣只是改變順序return True, 不然return False
# s和t內容全是小寫英文字母

# By hash, time: O(n), space: O(26), 因字母最多就26種
# 將第一個字串s的內容建成hash, 走訪t確認是否一模一樣
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 注意只要長度不同必定False, 也避免t比s長造成True的情況
        if len(s)!=len(t):
            return False
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        for i in t:
            if i not in hash or hash[i]==0:
                return False
            else:
                hash[i] -= 1
        return True

# By sort, time: O(nlogn), space: O(logn)
# space = O(logn)原因是排序所花費的空間 
# 這題也可以將字串sort後確認是否相同
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
#         # 注意str沒有str.sort(), 而sorted()可以給str用但會回傳list, 且用法是sorted(str)而分.sorted()
#         # 變成list之後用"".join(list)轉回str
#         # split()是以指定符號為分隔, 默認是空白, 不能用在這種連續字元上
#         # 連續字元直接用list(str)轉換即可
#         s = "".join(sorted(s))
#         t = "".join(sorted(t))
#         idx = len(s)-1
#         while idx>=0:
#             if s[idx]!=t[idx]:
#                 return False
#             idx -= 1
#         return True
    
# @lc code=end

=======
#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
# 給兩字串s和t, 如果s和t的字元一模一樣只是改變順序return True, 不然return False
# s和t內容全是小寫英文字母

# By hash, time: O(n), space: O(26), 因字母最多就26種
# 將第一個字串s的內容建成hash, 走訪t確認是否一模一樣
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 注意只要長度不同必定False, 也避免t比s長造成True的情況
        if len(s)!=len(t):
            return False
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        for i in t:
            if i not in hash or hash[i]==0:
                return False
            else:
                hash[i] -= 1
        return True

# By sort, time: O(nlogn), space: O(logn)
# space = O(logn)原因是排序所花費的空間 
# 這題也可以將字串sort後確認是否相同
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
#         # 注意str沒有str.sort(), 而sorted()可以給str用但會回傳list, 且用法是sorted(str)而分.sorted()
#         # 變成list之後用"".join(list)轉回str
#         # split()是以指定符號為分隔, 默認是空白, 不能用在這種連續字元上
#         # 連續字元直接用list(str)轉換即可
#         s = "".join(sorted(s))
#         t = "".join(sorted(t))
#         idx = len(s)-1
#         while idx>=0:
#             if s[idx]!=t[idx]:
#                 return False
#             idx -= 1
#         return True
    
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
