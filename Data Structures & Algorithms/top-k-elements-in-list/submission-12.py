class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in hashmap.items():
            freq[value].append(key)
        
        result = []
        for l in freq[::-1]:
            for n in l:
                result.append(n)
                if len(result) == k:
                    return result