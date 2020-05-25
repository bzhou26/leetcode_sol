'''
- Leetcode problem: 957

- Difficulty: Medium

- Brief problem description:

    There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]


Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9

- Solution Summary:
There is a loop for the result, so check if the result equals to the previous result. If so get the remainder.

- Used Resources:

--- Bo Zhou
'''


'''
Solution one: (Timeout)
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        oldCells = cells[:]
        newCells = [0]
        for i in range(N):
            for k in range(1, len(cells) - 1):
                if oldCells[k - 1] == oldCells[k + 1]:
                    newCells.append(1)
                else:
                    newCells.append(0)
            newCells.append(0)
            oldCells = newCells[:]
            newCells = [0]
        return oldCells
'''


class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        source, tmp = None, [0] * 8
        cycle, remainDays = 0, N

        while remainDays:
            for i in range(1, 7):
                tmp[i] = int(cells[i - 1] == cells[i + 1])

            if cycle == 0:
                source = tmp[::]
            elif source == tmp:
                remainDays %= cycle

            cells = tmp[::]
            cycle += 1
            remainDays -= 1

        return cells


if __name__ == "__main__":
    solution = Solution()
    testList = [0,1,0,1,1,0,0,1]
    print(solution.prisonAfterNDays(testList, 2000))