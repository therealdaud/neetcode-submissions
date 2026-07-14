class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            
            if num not in freq:
                freq[num] = 1

        for i in range(k):
            highest_k = max(freq, key = freq.get)
            ans.append(highest_k)
            del freq[highest_k]

        return ans