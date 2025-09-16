class Solution:
    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        deleted = 0
        backtracked = False
        lastChanged = 0
        left = 0
        right = 0
        i = -1
        while i < length // 2 - 1:
            i += 1
            if s[i + left] == s[length - 1 - i - right]:
                continue
            else:
                if backtracked:
                    print("Udh 2x diubah")
                    print(f"{s[i + left]}[{i + left}] dan {s[length - 1 - i - right]}[{length - 1 - i - right}]")
                    return False
                    continue
                print(f"{s[i + left]}[{i + left}] dan {s[length - 1 - i - right]}[{length - 1 - i - right}]")
                if deleted != 0:
                    print("Previously deleted")
                    i = lastChanged
                    left = 0
                    right = 0
                    backtracked = True

                if s[i + 1] == s[length - 1 - i] and deleted != -1:
                    left += 1
                    lastChanged = i
                    deleted = -1
                    right = 0
                elif s[i] == s[length - 2 - i] and deleted != 1:
                    right += 1
                    lastChanged = i
                    deleted = 1
                    left = 0
                else:
                    print("Kiri kanan tak bisa")
                    return False
        return True