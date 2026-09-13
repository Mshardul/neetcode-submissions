class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.append(str(len(strs)))
        return "\n".join(strs)

    def decode(self, s: str) -> List[str]:
        lst = s.split("\n")
        ln = int(lst.pop())
        if ln==0:
            return []
        return lst

