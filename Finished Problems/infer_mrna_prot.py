import functools
import operator
from rosalind_resources import codons

RNA_table = codons('RNA')

aa_count = {}
for abbr in RNA_table.values():
  if abbr == 'Stop':
    abbr = '-'
  if abbr not in aa_count:
    aa_count[abbr] = 1
  else:
    aa_count[abbr] += 1

with open('rosalind_mrna.txt', 'r') as text_obj:
  prot_string = text_obj.read().strip() + '-'

print(prot_string)

rna_strings = functools.reduce(operator.mul, [aa_count[aa] for aa in list(prot_string)])

print(rna_strings % 1000000)

# Desired Output: 12