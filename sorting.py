import random
# for elements in range(20):
#     lst.append(random.randint(0, 100))

test = [64, 69, 74, 91, 77, 47, 48, 81, 83, 23, 55, 95, 25, 59, 60, 63, 30, 31] # There 18 elements.




def solution(lst):
    temp = []
    swap = 0
    for item in range(len(lst)):
        # print(lst[item])
        # print(lst[item:])
        # print(f"The current value is {lst[item]} and the values after it are {lst[item+1:]}.")
        for things in lst[item+1:]:
            if lst[item] > things:
                index_of_things = lst.index(things)
                lst[item], lst[index_of_things] = lst[index_of_things], lst[item] 
                swap += 1
    
    print(f"Array is sorted in {swap} swaps.")
    print(f"First element: {lst[0]}")
    print(f"Last element: {lst[(len(lst))-1]}")
    return lst



solution(test)
print(test)
