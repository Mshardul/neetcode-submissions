class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occur = {}
        for ch in s:
            if ch not in occur:
                occur[ch] = 0
            occur[ch] += 1
        for ch in t:
            if occur.get(ch, 0)<1:
                return False
            occur[ch] -= 1
        for ch, occ in occur.items():
            if occ>0:
                return False
        return True