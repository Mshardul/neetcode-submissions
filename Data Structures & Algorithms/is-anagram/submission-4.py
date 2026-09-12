class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ sol1
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
        """

        n1 = len(s)
        n2 = len(t)
        if n1!=n2:
            return False
        
        occurs = {}
        for char in s:
            if char not in occurs:
                occurs[char] = 0
            occurs[char] += 1
        
        for char in t:
            if char not in occurs or occurs[char]==0:
                return False
            occurs[char] -= 1
        
        return True