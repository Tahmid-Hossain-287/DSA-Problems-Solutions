'''
The problem can be found here: https://www.hackerrank.com/challenges/30-sorting/problem
'''

test = [64, 69, 74, 91, 77, 47, 48, 81, 83, 23, 55, 95, 25, 59, 60, 63, 30, 31] # There 18 elements.




def solution(lst): # The function takes a list containing unsorted number as parameter.
    swap = 0 # Keeps track of how many times elements had to be swapped.
    for item in range(len(lst)): # We iterate number of times equal to the number of items of the given list.
        for things in lst[item+1:]: # We iterate the elements after the current element.
            if lst[item] > things: # We check if any element after the current element is smaller than the current element.
                index_of_things = lst.index(things) # Index of an element that is smaller and placed after the current element.
                lst[item], lst[index_of_things] = lst[index_of_things], lst[item] # Swaps the positions of both elements.
                swap += 1 # Increases with the number times swapping takes place.
    
    # The next three lines are according to the requirements of the problem.
    print(f"Array is sorted in {swap} swaps.")
    print(f"First Element: {lst[0]}")
    print(f"Last Element: {lst[(len(lst))-1]}")
    return lst



solution(test)
print(test)
