class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^\w]', '', s)
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            print("l<r")
            print("l before check: ", l)
            print("r before check: ", r)
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
            print("l: ", l)
            print("rk: ", r)
        return True
            
