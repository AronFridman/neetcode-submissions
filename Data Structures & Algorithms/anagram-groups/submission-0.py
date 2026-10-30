class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        anagrams = []

        for string in strs:
            sorted_string = tuple(sorted(string))
            if sorted_string not in groups:
                groups[sorted_string] = len(anagrams)
                anagrams.append([string])

            else:
                anagrams[groups[sorted_string]].append(string)
        return anagrams
