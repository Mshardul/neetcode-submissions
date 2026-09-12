class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for st in strs:
            st_sorted = ''.join(sorted(st))
            if st_sorted not in anagram_map:
                anagram_map[st_sorted] = []
            anagram_map[st_sorted].append(st)

        resp = []
        for st_sorted, sts in anagram_map.items():
            resp.append(sts)
        return resp

