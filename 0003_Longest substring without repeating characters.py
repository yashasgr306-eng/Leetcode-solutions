class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0

        for i in range(len(s)):
            current = ""

            for j in range(i, len(s)):
                if s[j] not in current:
                    current += s[j]

                    if len(current) > longest:
                        longest = len(current)
                else:
                    break

        return longest
