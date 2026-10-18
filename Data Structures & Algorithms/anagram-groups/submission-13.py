class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        group the anagrams, put in a hashmap. then turn the hashmap into an array
        """
        hashmap = {}
        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord("a")] += 1
            counts = tuple(counts)

            if counts not in hashmap:
                hashmap[counts] = [word]
            else: 
                hashmap[counts].append(word)
        
        result = list(hashmap.values())
        return result