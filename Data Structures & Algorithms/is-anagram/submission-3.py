class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_count = [0] * 26
        for i in range(len(s)):
            freq_count[ord(s[i]) - ord("a")] += 1
            freq_count[ord(t[i]) - ord("a")] -= 1
        
        for freq in freq_count:
            if freq != 0:
                return False
        return True