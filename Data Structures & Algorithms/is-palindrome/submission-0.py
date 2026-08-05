class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        char_array = []
        for char in s:
            if char.isalnum():
                char_array.append(char)
                


        left = 0
        right = len(char_array) - 1

        while left <= right:
            if char_array[left] == char_array[right]:
                left += 1
                right -= 1
            else:
                return False


        return True
            
