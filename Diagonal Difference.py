sample_input = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]


def diagonalDifference(arr):
    # Write your code here
    first_diagonal = 0
    second_diagonal = 0
    first_pos = 0
    second_pos = -1
    for _ in arr:
        first_diagonal += _[first_pos]
        first_pos += 1
    
    for _ in arr:
        second_diagonal += _[second_pos]
        second_pos += -1
        

if __name__ == "__main__":
    diagonalDifference(sample_input)