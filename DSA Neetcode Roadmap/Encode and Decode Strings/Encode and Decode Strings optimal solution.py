class Solution:

    def encode(self, strs: List[str]) -> str:
        result_string = ""
        for word in strs:
            result_string = result_string + str(len(word)) + "=" + word
        return result_string
    
    def decode(self, s: str) -> List[str]:
        strs = []
        word = ""
        i = 0
        while i < len(s):
            j = i
            while s[j] != "=":
                j += 1
            print((s[i:j]))
            length = int(s[i:j])
            strs.append(s[j+1: j + 1 + length])
            i = j + 1 + length
        return strs