class Solution:
    def longestPalindrome(self, s: str) -> str:
        strlen = len(s)
        left = 0
        right = strlen
        longestLeft = left
        longestRight = right
        tempLongest = 0
        while right > 0:
            for i in range(strlen - right + 1):
                isPalindrome = True
                for j in range(left, right // 2):
                    if s[left + i + j] == s[right + i - j - 1]:
                        continue
                    else:
                        isPalindrome = False
                        break
                if isPalindrome:
                    if right - left > tempLongest:
                        longestRight = right + i
                        longestLeft = left + i
                        tempLongest = longestRight - longestLeft
                        break
            if tempLongest >= right:
                break
            right -= 1
        return s[longestLeft:longestRight]