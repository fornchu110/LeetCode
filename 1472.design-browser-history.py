<<<<<<< HEAD
#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class ListNode:
    def __init__(self, val, prev=None, next= None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps>0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps>0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end
=======
#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class BrowserHistory:

    def __init__(self, homepage: str):
        

    def visit(self, url: str) -> None:
        

    def back(self, steps: int) -> str:
        

    def forward(self, steps: int) -> str:
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end
>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215

