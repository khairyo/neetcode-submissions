class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        group the anagrams, put in a hashmap. then turn the hashmap into an array
        """
        hashmap = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [word]
            else: 
                hashmap[sorted_word].append(word)
        # now we have a hashmap of key = sorted word, values = array of the words
        
        result = list(hashmap.values())
        return result