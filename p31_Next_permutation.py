'''
- Leetcode problem: 31

- Difficulty: Medium

- Brief problem description:

    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

- Solution Summary:
1. Search from end of list to the beginning of the list.
    If found nums[i] > nums[i-1]
    swap nums[i] and the first number which is larger than nums[i] from the end of the list
2. Sort the list from the nums[i+1] to the end of the list ASC.
    If no swap. sort the whole list

- Used Resources:

--- Bo Zhou

'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        swapDone = False
        while i >= 0:
            i -= 1
            if i < 0:
                break
            if nums[i + 1] > nums[i]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[i] < nums[j]:
                        self.swapNum(i, j, nums)
                        swapDone = True
                        break
                if swapDone:
                    break
        listNeedSort = nums[i + 1:]
        list.sort(listNeedSort)
        for k in range(len(listNeedSort)):
            nums[i + 1 + k] = listNeedSort[k]
        return

    def swapNum(self, i, j, nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return

if __name__ == "__main__":
    solution = Solution()
    testList = [1, 3, 2]
    solution.nextPermutation(testList)
    print(testList)