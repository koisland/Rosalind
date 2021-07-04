from rosalind_resources import unpack_fasta

fasta = '>Rosalind_24\nTCAATGCATGCGGGTCTATATGCAT'
# fasta = '>Rosalind_24\nTCAATGCATGCGGGTCTATATGCAT\n>Rosalind_25\nGGGGTCGGGAATGCATGCCAT\n>Rosalind_26\nTCAATGGTCTATATGCAT'
# replace with readlines f(x) with real file

bp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
site = {}

dna_strings = unpack_fasta('rosalind_revp.txt')
# dna_strings = unpack_fasta_str(fasta)

for dna in dna_strings.values():
  print(dna)
  for pos, nt in enumerate(dna, 1):
    if pos != len(dna):
      if bp[nt] == dna[pos]:
        try:
          for i in range(1, 6):
            if bp[dna[pos-i-1]] == dna[pos+i]:
              site[f"{pos-i} {len(dna[pos-i-1:pos+i+1])}"] = dna[pos-i-1:pos+i+1]
            else:
              break
        except IndexError:
          pass

[print(key) for key in site.keys()]
#position and length of every reverse palindrome