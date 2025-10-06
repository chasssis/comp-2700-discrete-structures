#Charles Stevens
#COMP 2700 section 001

from copy import deepcopy
from random import randint
from time import process_time

#Problem 1

def power_set(S):
    #base case
    if len(S) == 0:
        return [[]]

    #recursive step:
    #pop last element
    x = S.pop()

    #recursive call on remaining list
    subsets_without_x = power_set(S)

    #make copies of subsets & add x
    subsets_with_x = deepcopy(subsets_without_x)
    for subset in subsets_with_x:
        subset.append(x)

    #reinstate x in S
    S.append(x)

    #combine and return
    return subsets_without_x + subsets_with_x

#-------------------------------------------------------------------------------
#Problem 2

def find_optimal_subset(E, m):
    #get all subsets of experiments
    all_subsets = power_set(E)

    #define variables for checking
    best_subset = []
    best_value = 0
    best_mass = 0

    #evaluate each subset
    for subset in all_subsets:
        total_mass = sum(exp[1] for exp in subset)
        total_value = sum(exp[2] for exp in subset)

        # check if within mass limit and better than current best
        if total_mass <= m and total_value > best_value:
            best_value = total_value
            best_mass = total_mass
            best_subset = subset

    # print results
    print("Optimal subset of experiment IDs: ", [exp[0] for exp in best_subset])
    print("Total value rating: ", best_value)
    print("Total mass: ", best_mass)

#-----------------------------------------------------------------------------------
#Problem 3

if __name__ == '__main__':
    #test Problem 1
    print("Test for power_set()")
    print("\n")

    #test for base case:
    A = []
    result_A = power_set(A)
    print("power_set([]) =", result_A)
    print("Original list after calling:", A)

    #test with list of length 2
    B = [1, 2]
    result_B = power_set(B)
    print("\npower_set([1, 2]) =", result_B)
    print("Original list after calling:", B)

    #test with list of length 3
    C = [1, 2, 3]
    result_C = power_set(C)
    print("\npower_set([1, 2, 3]) =", result_C)
    print("Original list after calling:", C)

    #test with list of length 5
    D = [1, 2, 3, 4, 5]
    result_D = power_set(D)
    print("\npower_set([1, 2, 3, 4, 5]) =", result_D)
    print("Original list after calling:", D)

    #test problem 2
    print("\nTest for find_optimal_subset()")


    E = [
            [1, 36, 5],
            [2, 264, 9],
            [3, 188, 6],
            [4, 203, 8],
            [5, 104, 8],
            [6, 7, 6],
            [7, 92, 2],
            [8, 65, 8],
            [9, 25, 3],
            [10, 170, 6],
            [11, 80, 7],
            [12, 22, 4]
        ]
    
    m = 700  # payload capacity

    find_optimal_subset(E, m)

#-----------------------------------------------------------------------------------
#Problem 4
#test with 24 random experiments

print("\nPerformance test with 24 random experiments:")
print("\n") 

#generate experiments
E24 = [[i + 1, randint(5, 300), randint(1, 10)] for i in range(24)]
payload_capacity = 1500  #arbitrary

print("Generated 24 random experiments.")
print("Timing brute-force optimization:")

start_time = process_time()
find_optimal_subset(E24, payload_capacity)
end_time = process_time()

elapsed = end_time - start_time
print(f"\nElapsed time: {elapsed:.2f} seconds")
print("(Reference: ~78 seconds on a 7800x3d)")