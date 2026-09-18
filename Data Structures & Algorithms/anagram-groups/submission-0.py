class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for string in strs:
            canonical = ''.join(sorted(string))

            if (canonical in anagram):
                anagram[canonical].append(string)
            else:
                anagram[canonical]=[string]

        return list(anagram.values())