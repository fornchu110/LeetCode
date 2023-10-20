#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
# By double stack, �����ϥΨ��stack�ӹ�@�@��queue 
# ������Jstack�M��Xstack
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # ��l�ƨ��stack, ��Jstack�M��Xstack
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # �s�����i�J��Xstack
        self.inStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # �p�G��stack���O�Ū�
        if self.empty():
            return None

        # �p�G��Xstack������, �^�ǿ�Xstack������
        if self.outStack:
            return self.outStack.pop()
        # ��Xstack����, �N��Jstack�������e���Xstack
        else:
            while self.inStack:
                val = self.inStack.pop()
                self.outStack.append(val)
            return self.outStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # �ϥ�pop
        res = self.pop()
        # pop�X�Fres�ҥH�n�A�K�[�^�h
        self.outStack.append(res)
        return res


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # ���stack����, queue�~��
        if not(self.inStack or self.outStack):
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end