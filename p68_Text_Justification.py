'''
- Leetcode problem: 68

- Difficulty: Hard

- Brief problem description:

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and
is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces
' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide
evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

- Solution Summary:

- Used Resources:

--- Bo Zhou
'''


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        lines = []
        lines_c = []
        count = 0
        cur = []
        for w in words:
            if count + len(w) + len(cur) <= maxWidth:
                count += len(w)
                cur.append(w)
            else:
                lines.append(cur)
                lines_c.append(count)
                cur = [w]
                count = len(w)
        for i in range(len(lines)):
            spaces = maxWidth - lines_c[i]
            pos = max(len(lines[i]) - 1, 1)
            for j in range(spaces):
                lines[i][j % pos] += ' '
            result.append("".join(lines[i]))

        last_line = " ".join(cur)
        last_line = last_line + (maxWidth - len(last_line)) * " "
        result.append(last_line)

        return result
