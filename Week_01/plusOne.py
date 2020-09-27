class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # n=len(digits)

        for i in range(len(digits) - 1, -1, -1):#==for i in range(1, len(digits)+1) digits[-i]
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits