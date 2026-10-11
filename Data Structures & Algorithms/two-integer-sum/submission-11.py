class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in nums:
            diff = target - i
            hashmap[i] = diff

        for k, v in hashmap.items():
            if k != v:
                if v in nums:
                    return [nums.index(k), nums.index(v)]
            if k == v and len(set(nums))!=len(nums):
                index = len(nums) - 1 - nums[::-1].index(v)
                return [nums.index(k), index]

            
        
        