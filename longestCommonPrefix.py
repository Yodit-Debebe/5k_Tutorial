class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        res = ""
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return res
            res += shortest[i]
        return res
