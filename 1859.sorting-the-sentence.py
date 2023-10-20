#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
# By split, time: O(n), space: O(n), n是字串s的長度
# 要將句子依照裡面字串提供的idx做排序
class Solution:
    def sortSentence(self, s: str) -> str:
        # split()將字串轉換成list並以空白分隔list的元素
        s = s.split()
        # 句子內字串的數量
        n = len(s)  
        # 初始化res, 因為要像是index array利用需要先建大小為n的list
        # res = [0]*n也有一樣效果, 不影響
        res = ["" for i in range(n)] 
        # 從頭走訪, 檢查每個字串提供的數字做為存入res的index, 因是1開始所以要-1
        # Ex: This1放入res[0]
        for i in s:
            # i[:-1]是python的切片, 前面是取閉區間, 後面是取開區間
            # 所以-1原以為是倒數第一個元素實際上是取倒數第二個
            # Ex: i = This1, i[:-1] = This
            # 而i的index實際上餘i[-1]也就是倒數第一個的位置提供
            # i[1]-1就是因上面說的, 提供的index從1開始而res從0開始
            res[int(i[-1])-1] = i[:-1]
        # 用" ".join將res從list轉換成str並return
        # 因句子中的字串會以空白間隔, 所以是" "
        return " ".join(res)
        
# @lc code=end

