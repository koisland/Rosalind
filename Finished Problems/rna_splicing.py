import pprint
from rosalind_resources import unpack_fasta, codons

strings = unpack_fasta('rosalind_splc.txt')
pre_mrna = list(strings.values())[0]
introns = list(strings.values())[1:]
mrna = pre_mrna
for intron in introns:
  mrna = mrna.replace(intron, '')

# NOTE: Should replace dna with uracils.

print(pre_mrna, len(pre_mrna))
nt_removed = sum([len(intron) for intron in introns])
print(f'\n{nt_removed} nts lost by intron removal.\n')
print(mrna, len(mrna))

dna_codons = codons('DNA')
protein = ''
for pos, nt in enumerate(mrna[:-2]):
  if pos % 3 == 0:
    protein += dna_codons[mrna[pos:pos+3]]
    
print(f"\nProtein:\n{protein.strip('Stop')}")
