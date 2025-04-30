class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary_number = str(bin(n))
        print(binary_number[2:])
        binary_complement = ""
        for i in binary_number[2:]:
            if i == "0":
                binary_complement += "1"
            elif i == "1":
                binary_complement +="0"
        
        decimal_number = int(binary_complement, 2)
        return decimal_number