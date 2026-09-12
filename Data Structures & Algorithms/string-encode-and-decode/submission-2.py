class Solution:

    def encode(self, strs: List[str]) -> str:
        count_lst = [str(len(st)) for st in strs]
        resp = "_".join(count_lst) + ":" + "".join(strs)
        return resp


    def decode(self, s: str) -> List[str]:
        if s==":":
            return []
        splits = s.split(":")
        count_str = splits[0]
        strs_str = ":".join(splits[1:])
        count_lst = [int(count) for count in count_str.split("_")]
        resp = []
        ind_start = 0
        for count in count_lst:
            ind_end = ind_start + count
            resp.append(strs_str[ind_start:ind_end])
            ind_start = ind_end
        return resp

