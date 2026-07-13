class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for str in strs:

            if "".join(sorted(str)) not in group:
                group["".join(sorted(str))] = []

            if "".join(sorted(str)) in group:
                group["".join(sorted(str))].append(str)
            
            

        return list(group.values())

        

            