#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
class SmallestInfiniteSet:
    def __init__(self):
        self.pq = []
        for i in range(1, 1001):
            heapq.heappush(self.pq, i)

    def popSmallest(self):
        if self.pq:
            return heapq.heappop(self.pq)
        return -1

    def addBack(self, num):
        if num not in self.pq:
            heapq.heappush(self.pq, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

