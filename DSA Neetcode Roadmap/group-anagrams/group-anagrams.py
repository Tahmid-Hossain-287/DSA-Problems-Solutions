class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        thisdict = {}
        for item in strs:
            sorted_item = "".join(sorted(item))
            
            if sorted_item not in thisdict:
                thisdict[sorted_item] = []
                thisdict[sorted_item].append(item)
            else:
                thisdict[sorted_item].append(item)
        return list(thisdict.values())