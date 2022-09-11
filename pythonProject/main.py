from itertools import product, permutations, combinations, combinations_with_replacement


def print_results(data):
    print(type(data))
    for n in data:
        print(n, end=', ')
    print()


list_a = ['a', 'b', 'c']
list_b = [1, 2, 3]
cartesian_product = product(list_a, list_b)
print_results(cartesian_product)

p_1 = permutations("ABC")
print_results(p_1)

p_2 = permutations("ABC", r=2)
print_results(p_2)

c_1 = combinations("ABC", r=2)
print_results(c_1)

c_2 = combinations("ABC", r=3)
print_results(c_2)

c_3 = combinations((1, 2, 3), r=2)
print_results(c_3)

c_4 = combinations_with_replacement((1, 2, 3), r=2)
print_results(c_4)