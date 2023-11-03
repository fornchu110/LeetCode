#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
# 給字串s, return字串s的這些元素能組成的最長迴文字串長度
# 也就是不用在乎先後順序, 只看排列組合後能組成的迴文
# Ex: abccccdd最長能組成dccaccd這一長度為7的迴文

# By hash and greedy, time: O(n), space: O(S), S為s中不重複的字元種類
# 注意可能有字串全部都由同一個元素構成
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # res是最後答案的最長長度, hash用來記錄不同元素出現次數
        res = 0
        hash = dict()
        # 走訪s紀錄每個元素出現的次數
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        # 記住hash用hash.items()同時走訪key和value
        for key, value in hash.items():
            # 不需要這個, 因為後面做//2本來就會把0和1變成0, 再*2也是0
            # if value>=2:
            # value//2<<1來去掉value中多餘的1, Ex: c有3個但迴文只需要2個
            res += value//2<<1
            # 用這段就不用return後那些, 因為在找是否有1個元素當迴文中央也只會找一次
            # 而那一次就是在元素出現奇數個當下能找, 且只在res為偶數個時需要找
            # 省下一次for迴圈的時間
            if res&1==0 and value&1==1:
                res += 1
        return res
            # 同時將該value減掉
            # hash[key] -= value//2<<1
        # 用hash.values()只走訪value, 也可以用hash.keys()只走訪key
        # 裡面所有key的value不是0就是1
        # for value in hash.values():
            # 只要有元素剩下一個, 就可以拿來當迴文正中央的元素
            # if value==1:
            #     return res+1
        
# @lc code=end

