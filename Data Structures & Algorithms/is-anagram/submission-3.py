class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occur_s = {}
        occur_t = {}

        for char in s:
            if char not in occur_s:
                occur_s[char] = 0
            occur_s[char] += 1
        
        for char in t:
            if char not in occur_t:
                occur_t[char] = 0
            occur_t[char] += 1

        chars_s = set(occur_s)
        chars_t = set(occur_t)

        if len(chars_s) != len(chars_t):
            return False
        
        for char in chars_s:
            if occur_s.get(char, 0) != occur_t.get(char, 0):
                return False

        return True
        