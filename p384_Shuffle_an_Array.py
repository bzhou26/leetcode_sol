'''
- Leetcode problem: 384

- Difficulty: Medium

- Brief problem description:

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums[:]
        self.arr = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.arr)):
            l = i
            r = len(self.arr) - 1 - i
            ranLen = random.randint(0, max(l, r))
            ranDirect = 1
            j = i
            if ranLen <= min(l, r):
                ranDirect = random.randint(0, 1)
            if l > r:
                if ranDirect == 1:
                    j = i - ranLen
                else:
                    j = i + ranLen
            else:
                if ranDirect == 1:
                    j = i + ranLen
                else:
                    j = i - ranLen
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        return self.arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()