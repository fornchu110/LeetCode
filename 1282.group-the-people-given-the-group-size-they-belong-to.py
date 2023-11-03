<<<<<<< HEAD
#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
# By hash table, time: O(n), space: O(n)
# input內元素是各id之人所在group的人數, 要return照input分配id的分組
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = list()
        # res裡面放著各個groupsize為i的group
        # hash[i]就是為了當作找groupsize為i之group在res中的位置的index
        # 也就是說res[hash[i]]即為res中groupsize為i的group
        # 所以hash[i]在size為i的group滿了才會增加
        hash = dict()
        for id, i in enumerate(groupSizes):
            # 當i不在hash內或上一個group滿時, append新的id進res
            # len(res[hash[i]])==i就是用來判斷res內size為i的group滿了沒
            if i not in hash or len(res[hash[i]])==i:
                hash[i] = len(res)
                res.append([id])
            # 在res[hash[i]]未滿時, 繼續將i之id append進去
            else:
                res[hash[i]].append(id)
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
# By hash table, time: O(n), space: O(n)
# input內元素是各id之人所在group的人數, 要return照input分配id的分組
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = list()
        # res裡面放著各個groupsize為i的group
        # hash[i]就是為了當作找groupsize為i之group在res中的位置的index
        # 也就是說res[hash[i]]即為res中groupsize為i的group
        # 所以hash[i]在size為i的group滿了才會增加
        hash = dict()
        for id, i in enumerate(groupSizes):
            # 當i不在hash內或上一個group滿時, append新的id進res
            # len(res[hash[i]])==i就是用來判斷res內size為i的group滿了沒
            if i not in hash or len(res[hash[i]])==i:
                hash[i] = len(res)
                res.append([id])
            # 在res[hash[i]]未滿時, 繼續將i之id append進去
            else:
                res[hash[i]].append(id)
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
