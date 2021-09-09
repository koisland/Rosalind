from rosalind_resources import unpack_fasta

dna = unpack_fasta('rosalind_tran.txt')
s1 = list(dna.values())[0]
s2 = list(dna.values())[1]

transitions = 0
transversions = 0

transition_dict = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}

for nt1, nt2 in zip(s1, s2):
  if transition_dict[nt1] == nt2:
    transitions += 1
  elif nt1 != nt2 and transition_dict[nt1] != nt2:
    transversions += 1

R_s1s2 = transitions/transversions
print(R_s1s2)
  