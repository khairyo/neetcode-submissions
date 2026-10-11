class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
for duplicates - qn says have one valid answer always. so return indexes of those two numbers - ig find index of the first one, then find index of the second where it's diff from the first.
        """
        # put all array numbers (key) in a hashmap, and their values are the target - current number
        hashmap = {}
        for i in nums:
            diff = target - i
            hashmap[i] = diff
        
        # for the current key, if its value is in the array, then return index of current key and its value. 
        for k, v in hashmap.items():
            if k != v:
                if v in nums:
                    return [nums.index(k), nums.index(v)]
            if k == v and len(set(nums))!=len(nums):
                index = len(nums) - 1 - nums[::-1].index(v)
                return [nums.index(k), index]

            
        
        