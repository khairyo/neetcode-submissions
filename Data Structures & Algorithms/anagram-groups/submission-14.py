class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

        results = list(hashmap.values())
        return results