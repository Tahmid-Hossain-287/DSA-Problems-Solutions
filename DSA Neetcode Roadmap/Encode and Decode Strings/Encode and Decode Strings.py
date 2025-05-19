class Solution:

    def encode(self, strs: List[str]) -> str:
        result_string = ""
        for word in strs:
            result_string = result_string + word
            # if word != strs[-1]:
            result_string = result_string + "="
        return result_string

    def decode(self, s: str) -> List[str]:
        strs = []
        word = ""
        for character in s:
            if character != "=":
                word = word + character
            elif character == "=":
                strs.append(word)
                word = ""
        return strs