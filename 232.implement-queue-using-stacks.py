#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
# By double stack, 必須使用兩個stack來實作一個queue 
# 分為輸入stack和輸出stack
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 初始化兩個stack, 輸入stack和輸出stack
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # 新元素進入輸出stack
        self.inStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 如果兩stack都是空的
        if self.empty():
            return None

        # 如果輸出stack不為空, 回傳輸出stack的元素
        if self.outStack:
            return self.outStack.pop()
        # 輸出stack為空, 將輸入stack的元素送到輸出stack
        else:
            while self.inStack:
                val = self.inStack.pop()
                self.outStack.append(val)
            return self.outStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # 使用pop
        res = self.pop()
        # pop出了res所以要再添加回去
        self.outStack.append(res)
        return res


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # 兩個stack都空, queue才空
        if not(self.inStack or self.outStack):
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()