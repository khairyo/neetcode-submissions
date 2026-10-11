class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        # put all ch in s in the hashmap (key)
        # and the number of times it appears as the value
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else: 
                hashmap[i] += 1
        
        # now we move to t, and we first check if the keys are all the same. if not, return false. 
        # if all the same, then check the values: we decrease each one by one for each ch we go across in t, then if at the end all values are 0, return true. else reutrn false
        for n in t:
            if n not in hashmap:
                return False
            hashmap[n] -= 1
        
        # true if all 0
        results = all(value == 0 for value in hashmap.values())
        return results