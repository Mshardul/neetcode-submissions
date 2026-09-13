class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele_to_count = {}
        for num in nums:
            if num not in ele_to_count:
                ele_to_count[num] = 0
            ele_to_count[num] += 1
        
        count_to_ele = {}
        for ele, count in ele_to_count.items():
            if count not in count_to_ele:
                count_to_ele[count] = []
            count_to_ele[count].append(ele)
        
        counts = list(count_to_ele.keys())
        counts.sort()
        ind = len(counts)-1
        total_eles = []
        while ind>=0:
            count = counts[ind]
            curr_eles = count_to_ele[count]
            num_curr_eles = len(curr_eles)
            req = min(k-len(total_eles), num_curr_eles)
            total_eles.extend(curr_eles[:req])
            ind -= 1
        
        return total_eles

        