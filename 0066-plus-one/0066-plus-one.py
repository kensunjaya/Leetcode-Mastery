class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for i in range(length):
            if digits[length-i-1] + 1 == 10:
                digits[length-i-1] = 0
            else:
                digits[length-i-1] += 1
                return digits
        digits.insert(0, 1)
        return digits