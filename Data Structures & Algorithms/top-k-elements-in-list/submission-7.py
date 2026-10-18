class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        # we now have a hashmap where key = number, value = frequency of the number

        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in hashmap.items():
            freq[value].append(key)
        result = []
        count = 0
        for l in freq[::-1]:
            for num in l:
                result.append(num)
                if len(result) == k:
                    return result