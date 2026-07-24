class Solution:

    def encode(self, strs: List[str]) -> str: 
        enc = []
        for s in strs:
            enc.append(f"{len(s)}#{s}")
        encoded_string = "".join(enc)
        return encoded_string
            
            
    def decode(self, s: str) -> List[str]:
        '''now i have something like ["4#this2#is7#awesome"] and need to
        convert it to ["this", "is", "awesome"]
        - convert everything to invidual chars, look at first one and then
        loop through the following chars with the first item being the i in 
        the for loop. so in this example first is 4 for 4 times loop over next
        items and then put them together, now the issue is that they would include
        the # as well so we need to find a way to get rid of that # and the rest can then
        be concat into the word and stored in a list that would be returned at the end'''

        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            word = s[start:start + length]
            i = start + length
            res.append(word)
        return res
            
