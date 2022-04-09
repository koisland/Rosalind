import numpy as np


# import pprint

def find_closest(value, arr):
    # find abs diff between value and every item in arr.
    idx = np.abs(arr - value).argmin()
    return idx, arr[idx]


with open('rosalind_lgis.txt', 'r') as text_obj:
    # perm_n = text_obj.readlines()[1].strip()

    perm_str = '2 50 4 30 6 8 10 12 22 1411 16 18 3 17 20'
    # Low should be '2 4 6 8 10 12 16 17 20'
    # High should be '50 30 22 18 16' or '50 30 22 16/18 3'

perm_n = [int(num) for num in perm_str.split()]

perm_n = np.asarray(perm_n)

print(find_closest(2, perm_n))

# closest_vals = [find_closest(n, perm_n) for n in perm_n]
# print(closest_vals)
