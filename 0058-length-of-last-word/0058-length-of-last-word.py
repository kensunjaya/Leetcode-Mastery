class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letter_occurence = False
        length = 0
        for elm in s[::-1]:
            if elm != ' ' and not letter_occurence:
                letter_occurence = True
                length += 1
            elif elm != ' ' and letter_occurence:
                length += 1
            elif elm == ' ' and letter_occurence:
                break
        return length