class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        freq = {}
        length = len(strs)
        out = ""
        for i in range(len(strs[0])):
            freq[strs[0][i]+chr(i)] = 1
        
        for elms in strs[1:]:
            for j in range(len(elms)):
                key = elms[j]+chr(j)
                if key in freq:
                    freq[key] += 1
                else:
                    break
        print(freq)
        for key, value in freq.items():
            if length == value:
                out += key[0]
            else:
                return out
        return out
        