#
# @lc app=leetcode id=1845 lang=python3
#
# [1845] Seat Reservation Manager
#

# @lc code=start
# 實作一個座位管理系統, obj = SeatManager(n)傳入參數n代表有1~n個編號的座位
# 當obj.reserve()回傳可預約座位中編號最小的, 並將其設定為不可預約
# 當obj.unreserve(seatnumber)將指定編號的座位改為可預約

# By heap queue and greedy, Init time: O(n), reserve and unreserve time: O(1) or O(logn), space: O(n)
# O(1)原因是用continuous_last這個變數記住座位編號, 這個變數在預定座位編號都連續以及取消當下已預訂座位中編號最大者預約時有用
# 不需要在呼叫reserve()和unreserve()使用heap queue做push pop的話, 時間複雜度就只要O(1)
class SeatManager:
    def __init__(self, n: int):
        self.continuous_last = 0
        # heap queue用來在變數無法找出答案的情況做, 也就是被取消預約但編號非當下最大者
        # Ex: 已預定1、2、3, 這時取消2那2就會被放進來
        self.not_cotinuous_available_seat = []

    def reserve(self) -> int:
        # heap queue為空代表預約座位編號為連續時, 直接用continuous_last就能得出要return誰
        # Ex: 目前已預定1、2、3, 這時候再預定就是要預訂4
        if len(self.not_cotinuous_available_seat)==0:
            self.continuous_last += 1
            return self.continuous_last
        # 當非連續時, 要用heap queue找出可預定最小編號
        # Ex: 已預定1、3, 這時候continuous_last是3但實際上有2, 而2也就在這個heap queue內, 所以return 2
        return heapq.heappop(self.not_cotinuous_available_seat)

    def unreserve(self, seatNumber: int) -> None:
        # 取消的剛好是目前已預定最大編號
        # Ex: 已預定1、2、3, 這時候取消3剩1、2已預定, 那已預定的座位編號仍保持連續
        if seatNumber==self.continuous_last:
            self.continuous_last -= 1
        # 將會讓已預定編號不連續的座位加入heap queue
        else:
            heapq.heappush(self.not_cotinuous_available_seat, seatNumber)

# By heap queue, Init time: O(n), reserve and unreserve time:  O(logn), space: O(n)
# 用heap queue(priority queue)來實作, 避免每次新增刪除元素都重新排序, 得到較低的時間複雜度
# 記住這種固定拿最大最小的題型都可以用heap queue來解, python中heapqq([])來初始化heap queue
# python的heapq默認是min heap
# class SeatManager:
    # def __init__(self, n: int):
    #     # 將編號1~n初始化為一個list
    #     self.seat_heap_queue = [i for i in range(1, n + 1)]

    # def reserve(self):
    #     # 每次需要預約座位時就return heap queue中最小的元素
    #     return heapq.heappop(self.seat_heap_queue)

    # def unreserve(self, seatNumber):
    #     # 每次取消預約時就將取消的編號按排序重新加回heap queue
    #     heapq.heappush(self.seat_heap_queue, seatNumber)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end

