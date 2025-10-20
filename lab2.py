#CHARLES STEVENS - COMP 2700-001

def is_function(A, B, f):
    #check if all x are used only once
    check = set() #set for storing what values in the domain have been checked
    for pair in f:
        if len(pair) != 2:
            return False
        x, y = pair
        if x not in A or y not in B:
            return False
        if x in check:
            return False
        check.add(x)
    return set(check) == set(A)

def function_range(A, B, f):
    if not is_function(A, B, f):
        return None
    values = sorted({y for _, y in f})
    return values


def is_one_to_one(A, B, f):
    if not is_function(A, B, f):
        return None
    values = [y for _, y in f]
    return len(values) == len(set(values)) #checks that mapped values are the same as range

def is_onto(A, B, f):
    if not is_function(A, B, f):
        return None
    values = {y for _, y in f}
    return set(B) == values

def inverse(A, B, f):
    if not is_function(A, B, f):
        return None
    if not is_one_to_one(A, B, f) or not is_onto(A, B, f):
        return None
    inv = [[y, x] for x, y in f]
    return sorted(inv)

if __name__ == '__main__':
    print("=== Testing is_function ===")
    #true test case
    A = [1, 2, 3]
    B = [4, 5]
    f = [[1, 4], [2, 5], [3, 4]]
    print(is_function(A, B, f))

    #false: x=2 mapped twice
    f_bad1 = [[1, 4], [2, 5], [2, 4], [3,4]]
    print(is_function(A, B, f_bad1))  # False

    #false: no mapping for 3
    f_bad2 = [[1, 4], [2, 5]]
    print(is_function(A, B, f_bad2))  # False

    #false: extra element not in A
    f_bad3 = [[1, 4], [2, 5], [4, 4]]
    print(is_function(A, B, f_bad3))  # False

    #false: value not in B
    f_bad4 = [[1, 4], [2, 5], [3, 6]]
    print(is_function(A, B, f_bad4))  # False

    print("\n=== Testing function_range ===")
    print(function_range(A, B, f))  # [4, 5]
    print(function_range(A, B, f_bad1))  # None
    #range doesn't match B
    A2 = [1, 2]
    B2 = [4, 5, 6]
    f2 = [[1, 4], [2, 5]]
    print(function_range(A2, B2, f2))  # [4, 5]
    #multiple x to same y
    A3 = [1, 2, 3]
    B3 = [4, 5]
    f3 = [[1, 4], [2, 4], [3, 5]]
    print(function_range(A3, B3, f3))  # [4, 5]

    print("\n=== Testing is_one_to_one ===")
    print(is_one_to_one(A, B, f))  #false
    f4 = [[1, 4], [2, 5], [3, 6]]
    A4 = [1, 2, 3]
    B4 = [4, 5, 6]
    print(is_one_to_one(A4, B4, f4))  #true
    print(is_one_to_one(A, B, f_bad1))  #none

    print("\n=== Testing is_onto ===")
    print(is_onto(A, B, f))  #true
    print(is_onto(A2, B2, f2))  #false
    print(is_onto(A, B, f_bad1))  #none

    print("\n=== Testing inverse ===")
    #not a function
    print(inverse(A, B, f_bad1))  #none
    #valid function but not 1-1 or onto
    f5 = [[1, 4], [2, 4], [3, 4]]
    A5 = [1, 2, 3]
    B5 = [4]
    print(inverse(A5, B5, f5))  #none
    #1-1 but not onto
    f6 = [[1, 4], [2, 5]]
    A6 = [1, 2]
    B6 = [4, 5, 6]
    print(inverse(A6, B6, f6))  #none
    #onto but not 1-1
    f7 = [[1, 4], [2, 5], [3, 5]]
    A7 = [1, 2, 3]
    B7 = [4, 5]
    print(inverse(A7, B7, f7))  #none
    #bijective
    A8 = [1, 2, 3]
    B8 = [4, 5, 6]
    f8 = [[1, 6], [2, 5], [3, 4]]
    print(inverse(A8, B8, f8))  #[[4, 3], [5, 2], [6, 1]]