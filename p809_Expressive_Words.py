'''
- Leetcode problem: 809

- Difficulty: Medium

- Brief problem description:

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these
strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of
the following extension operation: choose a group consisting of characters c, and add some number of characters c to
the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get
"helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get
"helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension
operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy.



Example:
Input:
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.


Constraints:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        total = 0
        c1, c1_str = self.countStr(S)
        for w in words:
            c2, c2_str = self.countStr(w)
            if c2_str == c1_str:
                ext = True
                for i in range(len(c2_str)):
                    if (c1[i] < 3 and c1[i] != c2[i]) or c1[i] < c2[i]:
                        ext = False
                if ext:
                    total += 1

        return total

    def countStr(self, S):
        count1 = []
        count1_str = ''
        cur = ''
        cur_count = 0
        for c in S:
            if len(cur) > 0:
                if c == cur:
                    cur_count += 1
                else:
                    count1.append(cur_count)
                    count1_str += cur
                    cur_count = 1
                    cur = c
            else:
                cur_count = 1
                cur = c
        count1.append(cur_count)
        count1_str += cur

        return (count1, count1_str)
