class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            if word in seen:
                seen[word].append(strs[i])
            else:
                seen[word] = [strs[i]]
        return list(seen.values())