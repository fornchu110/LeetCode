#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start

#By lock
#三個thread競爭, 希望無論規定誰執行哪個都要first->second->third
#這題屬於race condition, 大家爭搶進入自己的print(critical section)
#讓三個function變synchronization(同步指大家要照順序一個一個完成, 而非同時做自己的)
from threading import Lock

class Foo:
    def __init__(self):
        #一開始設了兩個lock
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()
        #因預設firstJobDone上鎖, 只有first完成直行到release才把lock解鎖

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        #with+lock是python的lock使用方法
        #當try到firstJonDone解鎖了, 代表first執行完畢, 才能執行second下面的print
        with self.firstJobDone: 
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            #second完成, 將secondJobDone解鎖
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # Wait for the second job to be done.
        #與second地方同理, second做完了才能做third的print
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()

# @lc code=end

