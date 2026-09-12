class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """O(n) - 1 loop - with extra space"""
        visited = {}
        for ind, num in enumerate(nums):
            req = target-num
            if req in visited:
                return [visited[req], ind]
            visited[num] = ind
        return []
        