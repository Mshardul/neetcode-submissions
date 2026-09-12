class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {num: freq}
        num_to_freq_map = {}
        for num in nums:
            if num not in num_to_freq_map:
                num_to_freq_map[num] = 0
            num_to_freq_map[num] += 1
        print("num_to_freq_map: ", num_to_freq_map)
        
        # {freq: [num]}
        freq_to_num_map = {}
        for num, freq in num_to_freq_map.items():
            if freq not in freq_to_num_map:
                freq_to_num_map[freq] = []
            freq_to_num_map[freq].append(num)
        print("freq_to_num_map: ", freq_to_num_map)
            
        # descending sort all frequencies
        frequencies = list(freq_to_num_map.keys())
        frequencies.sort(reverse=True)
        print("frequencies: ", frequencies)
        
        # main function - formulate resp
        resp = []
        frequencies__ind = 0
        print(f"\n{"*"*5} Loop started {"*"*5}")
        while len(resp)<k and frequencies__ind<len(frequencies):
            print(frequencies__ind)
            freq = frequencies[frequencies__ind]
            print("freq: ", freq)
            nums_with_freq = freq_to_num_map[freq]
            print("nums_with_freq: ", nums_with_freq)
            resp.extend(nums_with_freq)
            print("resp: ", resp)
            frequencies__ind += 1
        
        return resp[:k]