class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        char_count = {}

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right],0) + 1 
            max_freq = max(char_count.values())

            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -=1
                left += 1

            max_len = max(max_len, right - left +1)

        return max_len