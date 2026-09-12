class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # occurance = {num: {set_of_indices}}
        occur = {}
        for ind, num in enumerate(nums):
            if num not in occur:
                occur[num] = set()
            occur[num].add(ind)

        # verify
        for ind, num in enumerate(nums):
            num_to_find = target - num
            target_indices = occur.get(num_to_find, None)
            if target_indices:
                for target_index in target_indices:
                    if ind == target_index:
                        continue
                    mn = min(ind, target_index)
                    mx = max(ind, target_index)
                    return [mn, mx]