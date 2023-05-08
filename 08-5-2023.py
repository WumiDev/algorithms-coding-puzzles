from itertools import permutations

def find_divisible_by_7_permutation(num_str):
    digits = [int(digit) for digit in num_str]
    perms = list(permutations(digits))
    print("Permutations:")
    for perm in perms:
        print(int(''.join(map(str, perm))))
    divisible_by_7_perms = [perm for perm in perms if int(''.join(map(str, perm))) % 7 == 0]
    if not divisible_by_7_perms:
        print("No permutation is divisible by 7")
    else:
        smallest_perm = min(divisible_by_7_perms)
        largest_perm = max(divisible_by_7_perms)
        avg = (int(''.join(map(str, smallest_perm))) + int(''.join(map(str, largest_perm)))) / 2
        print(f"Permutations ({''.join(map(str, smallest_perm))}, {''.join(map(str, largest_perm))}) are divisible by 7")
        print(f"The average between the smallest and largest permutation is: {avg:.2f}")

# Solving the code puzzle challenge with the 
num_str = '1867'
find_divisible_by_7_permutation(num_str)
