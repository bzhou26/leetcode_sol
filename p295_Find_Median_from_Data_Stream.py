'''
- Leetcode problem: 295

- Difficulty: Hard

- Brief problem description:

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the
median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if len(self.low) == 0:
            heapq.heappush(self.low, num * -1)
            return

        lowbound = self.low[0] * -1

        if len(self.low) == len(self.high):
            upperbound = self.high[0]
            if num <= upperbound:
                heapq.heappush(self.low, num * -1)
            else:
                swap = heapq.heappop(self.high)
                heapq.heappush(self.low, swap * -1)
                heapq.heappush(self.high, num)
        else:
            if num > lowbound:
                heapq.heappush(self.high, num)
            else:
                swap = heapq.heappop(self.low) * -1
                heapq.heappush(self.low, num * -1)
                heapq.heappush(self.high, swap)

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (self.low[0] * -1 + self.high[0]) / 2
        else:
            return self.low[0] * -1

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
