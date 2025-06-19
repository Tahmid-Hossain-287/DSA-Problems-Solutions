class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)%2) != 0:
            return False

        first_part = (s[:int(len(s)/2)])
        second_part = (s[int(len(s)/2):])

        left = 0
        right = len(s) - 1

        while left < right:
            if (
                not((s[left] == "(") and (s[right] == ")")) 
                or not((s[left] == "{") and (s[right] == "}")) 
                or not((s[left] == "[") and (s[right] == "]"))
            ):
                return False
            else:
                left += 1
                right -= 1
        return True