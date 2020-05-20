class Solution:
    def partitionLabels(self, S):
        last = dict()
        for i in range(len(S) - 1, -1, -1):
            if not last.get(S[i]):
                last[S[i]] = i
        start = 0
        end = 0
        current = 0
        result = []
        while current < len(S):
            thisEnd = end
            if last[S[current]]:
                thisEnd = last[S[current]]
            end = max(thisEnd, end)
            if current == end:
                result.append(end - start + 1)
                start = current + 1
                end = current + 1
            current += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    testStr = 'ababcbacadefegdehijhklij'
    print(solution.partitionLabels(testStr))