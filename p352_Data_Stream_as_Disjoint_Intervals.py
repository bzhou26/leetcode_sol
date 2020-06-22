'''
- Leetcode problem: 352

- Difficulty: Hard

- Brief problem description:

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of
disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]


Follow up:

What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ih = []  # interval heap

    def addNum(self, val: int) -> None:
        heapq.heappush(self.ih, [val, val])

    def getIntervals(self) -> List[List[int]]:
        newh = []
        while self.ih:
            newInter = heapq.heappop(self.ih)
            if newh and newh[-1][1] + 1 >= newInter[0]:
                newh[-1][1] = max(newh[-1][1], newInter[1])
            else:
                heapq.heappush(newh, newInter)
        self.ih = newh
        return self.ih

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()