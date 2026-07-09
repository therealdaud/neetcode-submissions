class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_t = {}
        seen_s = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in seen_s:
                seen_s[char] =+ 1
            else: 
                seen_s[char] = {}
            

        for char in t:
            if char in seen_t:
                seen_t[char] =+ 1
            else: 
                seen_t[char] = {}

            

        if seen_t == seen_s:
            return True

        return False


        