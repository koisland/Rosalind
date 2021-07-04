from itertools import product

with open('rosalind_lexf.txt', 'r') as text_obj:
  ord_alph, num = text_obj.readlines()
  ord_alph = ord_alph.split()

# [print(''.join(perm)) for perm in product(ord_alph, repeat=int(num))]  

# Expected Result:
# AA
# AC
# AG
# AT
# CA
# CC
# CG
# CT
# GA
# GC
# GG
# GT
# TA
# TC
# TG
# TT

# Rosalind Solution
k_mer = ord_alph

for l in range(int(num)-1):
  k_mer =  [i+j for i in ord_alph for j in k_mer]

for i in k_mer: 
  print(i)