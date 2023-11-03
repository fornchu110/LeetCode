<<<<<<< HEAD
#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
# 給一個字串s, 要求將其照順序分割為不同子字串, 子字串內不能有重複的字符

# By hash, time: O(n), space: O(n)
# 建立hash, 當此次子字串遇到不存在的字母就記錄並繼續, 遇到已存在的就代表結束上一個, 建立新的hash
# 也可以用set製作hash, set.clear(), set.add()可以加入
class Solution:
    def partitionString(self, s: str) -> int:
        hash = {}
        # 默認為何是1?因給s長度至少是1, 代表至少會有一個字元字串
        res = 1
        for i in s:
            # 遇到重複的就代表要建一個新的子字串, 並且清衝
            if i in hash:
                res += 1
                hash = {}
            # 無論是否重複, 都要將i記錄進hash
            # 沒重複時記錄下來才能檢查
            # 重複時因碰到此時清空了hash, 仍要將這次碰到的字元記錄進hash避免遺失
            hash[i] = 1
        return res

# By bitwise, time: O(n), space: O(1)
# 利用32個bit記錄檢查26個字母是否存在
# a放在第0個位元, z放在第25個位元以此類推, 用左移1做記錄和檢查
# 不知為何時間空間都比hash差
# class Solution:
#     def partitionString(self, s: str) -> int:
#         res = 1
#         tmp = 0
#         for i in s:
#             # 和'a'的ASCII code比較相對位置
#             index = ord(i)-ord('a')
#             # mask就是這次的字元對應的位置
#             mask = 1<<index
#             # 出現重複字母, 那res+1並且將tmp = mask等同記錄了這次的字母
#             if tmp&mask:
#                 res += 1
#                 tmp = mask
#             else:
#                 # 出現不重複字母, 那就單純把mask記錄上去為1
#                 tmp |= mask
#             # 其實直接在外面這邊寫tmp |= mask, if和else內的tmp拿掉應該也行
#         return res



# @lc code=end

=======
#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
# 給一個字串s, 要求將其照順序分割為不同子字串, 子字串內不能有重複的字符

# By hash, time: O(n), space: O(n)
# 建立hash, 當此次子字串遇到不存在的字母就記錄並繼續, 遇到已存在的就代表結束上一個, 建立新的hash
# 也可以用set製作hash, set.clear(), set.add()可以加入
class Solution:
    def partitionString(self, s: str) -> int:
        hash = {}
        # 默認為何是1?因給s長度至少是1, 代表至少會有一個字元字串
        res = 1
        for i in s:
            # 遇到重複的就代表要建一個新的子字串, 並且清衝
            if i in hash:
                res += 1
                hash = {}
            # 無論是否重複, 都要將i記錄進hash
            # 沒重複時記錄下來才能檢查
            # 重複時因碰到此時清空了hash, 仍要將這次碰到的字元記錄進hash避免遺失
            hash[i] = 1
        return res

# By bitwise, time: O(n), space: O(1)
# 利用32個bit記錄檢查26個字母是否存在
# a放在第0個位元, z放在第25個位元以此類推, 用左移1做記錄和檢查
# 不知為何時間空間都比hash差
# class Solution:
#     def partitionString(self, s: str) -> int:
#         res = 1
#         tmp = 0
#         for i in s:
#             # 和'a'的ASCII code比較相對位置
#             index = ord(i)-ord('a')
#             # mask就是這次的字元對應的位置
#             mask = 1<<index
#             # 出現重複字母, 那res+1並且將tmp = mask等同記錄了這次的字母
#             if tmp&mask:
#                 res += 1
#                 tmp = mask
#             else:
#                 # 出現不重複字母, 那就單純把mask記錄上去為1
#                 tmp |= mask
#             # 其實直接在外面這邊寫tmp |= mask, if和else內的tmp拿掉應該也行
#         return res



# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
