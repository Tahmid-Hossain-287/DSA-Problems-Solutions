class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)%2) != 0:
            return False

        first_part = (s[:int(len(s)/2)])
        second_part = (s[int(len(s)/2):])

        if first_part == second_part[::-1]:
            return True
        else:
            return False