#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start

#By lock
#�T��thread�v��, �Ʊ�L�׳W�w�ְ�����ӳ��nfirst->second->third
#�o�D�ݩ�race condition, �j�a���m�i�J�ۤv��print(critical section)
#���T��function��synchronization(�P�B���j�a�n�Ӷ��Ǥ@�Ӥ@�ӧ���, �ӫD�P�ɰ��ۤv��)
from threading import Lock

class Foo:
    def __init__(self):
        #�@�}�l�]�F���lock
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()
        #�]�w�]firstJobDone�W��, �u��first���������release�~��lock����

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        #with+lock�Opython��lock�ϥΤ�k
        #��try��firstJonDone����F, �N��first���槹��, �~�����second�U����print
        with self.firstJobDone: 
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            #second����, �NsecondJobDone����
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # Wait for the second job to be done.
        #�Psecond�a��P�z, second�����F�~�వthird��print
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()

# @lc code=end

