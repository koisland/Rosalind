from rosalind_resources import unpack_fasta
from itertools import product

dna = list(unpack_fasta('rosalind_kmer.txt').values())[0]

kmers = {}
nt = ['A', 'T', 'G', 'C']
for prod in product(nt, nt, nt , nt):
  kmers[''.join(prod)] = 0

for pos in range(0, len(dna) - 4):
  if dna[pos:pos + 4] in kmers:
    kmers[dna[pos:pos + 4]] += 1
print(sorted(kmers))
print(' '.join([str(kmers[kmer]) for kmer in sorted(kmers)]))

