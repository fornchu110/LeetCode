<<<<<<< HEAD
#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
# 給字串word和目標ch, 將word中第一次出現ch以前的部分反轉
# Ex: word: abcdefd, ch: d, return: dcbaefd

# By string processing, time: O(n), space: O(1) 
# 利用python切片的方式處理
# 若是c語言使用double pointer, 用strchr()找到ch後, 使用一個pointer指向開頭一個指向ch所在位置
# 在開頭<ch位置為條件, 分別交換位置所存放的字元並將開頭++, ch--, 當開頭>=ch位置便代表交換完畢
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # 首先找出ch第一次出現的位置, find找到ch的index
        # 而因切片[a:b]只會處理到b前一個, 所以要+1, 切片[a:b+1]才會a~b+1所有字元
        # Ex: word: abcdefd, ch: d, ch在index3, i = 4
        i = word.find(ch)+1
        # 找到ch所在後, return分成兩個部分, 反轉的和未反轉的
        # word[:i]代表取word開頭到ch, 後面再對這個字串做[::-1]也就是反轉
        # 反轉處理完後, +word[i]也就是ch以後的部分即可
        # 所以注意切片的概念是((word[:i])[::-1])
        # 不能用word[:i:-1], 這樣變成倒著走訪到i之下一個字元停止
        # Ex: word: abcdefd, ch: d, word[:i:-1] = df
        return word[:i][::-1]+word[i:]
        
# @lc code=end

=======
#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
# 給字串word和目標ch, 將word中第一次出現ch以前的部分反轉
# Ex: word: abcdefd, ch: d, return: dcbaefd

# By string processing, time: O(n), space: O(1) 
# 利用python切片的方式處理
# 若是c語言使用double pointer, 用strchr()找到ch後, 使用一個pointer指向開頭一個指向ch所在位置
# 在開頭<ch位置為條件, 分別交換位置所存放的字元並將開頭++, ch--, 當開頭>=ch位置便代表交換完畢
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # 首先找出ch第一次出現的位置, find找到ch的index
        # 而因切片[a:b]只會處理到b前一個, 所以要+1, 切片[a:b+1]才會a~b+1所有字元
        # Ex: word: abcdefd, ch: d, ch在index3, i = 4
        i = word.find(ch)+1
        # 找到ch所在後, return分成兩個部分, 反轉的和未反轉的
        # word[:i]代表取word開頭到ch, 後面再對這個字串做[::-1]也就是反轉
        # 反轉處理完後, +word[i]也就是ch以後的部分即可
        # 所以注意切片的概念是((word[:i])[::-1])
        # 不能用word[:i:-1], 這樣變成倒著走訪到i之下一個字元停止
        # Ex: word: abcdefd, ch: d, word[:i:-1] = df
        return word[:i][::-1]+word[i:]
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
