class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for st in strs:
            occur=[0]*26
            for char in st:
                ind = ord(char)-ord('a')
                occur[ind] += 1
            anagram_key = ",".join([str(count) for count in occur])
            if anagram_key not in res:
                res[anagram_key] = []
            res[anagram_key].append(st)
        return list(res.values())

        