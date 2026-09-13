class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        non_zero_prod = 1
        num_of_zero = 0
        for num in nums:
            if num==0:
                num_of_zero += 1
            else:
                non_zero_prod *= num
        
        ans = []
        for num in nums:
            if num==0:
                if num_of_zero>1:
                    ans.append(0)
                else:
                    ans.append(non_zero_prod)
            else:
                if num_of_zero>0:
                    ans.append(0)
                else:
                    ans.append(non_zero_prod//num)
        return ans
        