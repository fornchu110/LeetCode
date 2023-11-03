<<<<<<< HEAD
#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
#

# @lc code=start
# By array, time: O(n), space: O(n)
# 看不太懂, 以後再說
class OrderedStream:
    def __init__(self, n: int):
        self.stream = [""] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        stream_ = self.stream
        stream_[idKey] = value
        res = list()
        while self.ptr < len(stream_) and stream_[self.ptr]:
            res.append(stream_[self.ptr])
            self.ptr += 1
        
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end

=======
#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
#

# @lc code=start
# By array, time: O(n), space: O(n)
# 看不太懂, 以後再說
class OrderedStream:
    def __init__(self, n: int):
        self.stream = [""] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        stream_ = self.stream
        stream_[idKey] = value
        res = list()
        while self.ptr < len(stream_) and stream_[self.ptr]:
            res.append(stream_[self.ptr])
            self.ptr += 1
        
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
