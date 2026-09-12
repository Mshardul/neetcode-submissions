class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_exists: bool = False
        multiple_zero_exist: bool = False
        product_without_0: int = 1
        for num in nums:
            if num != 0:
                product_without_0 *= num
            elif zero_exists==False:
                zero_exists = True
            elif multiple_zero_exist==False:
                multiple_zero_exist = True
        
        resp = []
        for num in nums:
            if num == 0:
                if multiple_zero_exist:
                    resp.append(0)
                else:
                    resp.append(product_without_0)
            else:
                if zero_exists:
                    resp.append(0)
                else:
                    resp.append(product_without_0//num)
        return resp

        