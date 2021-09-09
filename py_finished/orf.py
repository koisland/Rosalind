import re
import pprint
from rosalind_resources import codons, unpack_fasta

codon_dict = codons('DNA')
entries = unpack_fasta('rosalind_orf.txt')

# pprint.pprint(codon_dict)
# pprint.pprint(entries)

def translate_orf(dna_dict):
  proteins = {}
  for entry, dna in dna_dict.items():
    proteins[entry] = []
    rev_dna = "".join(reversed(dna))
    rev_c_dna = rev_dna.replace('G', 'c').replace('C', 'g').replace('A', 't').replace('T', 'a').upper()
    for dna_var in (dna, rev_c_dna):
      for index, nt in enumerate(dna_var[:-2]):  # Forward
        start_rf = dna_var[index:index+3]

        if codon_dict[start_rf] == 'M':
          dna_string = dna_var[index:]
          protein = ''
          for index, nt in enumerate(dna_string[:-2]):
            if index % 3 == 0:
              # print(dna_string[index: index+3], codon_dict[dna_string[index: index+3]])
              protein += codon_dict[dna_string[index: index+3]]
              if codon_dict[dna_string[index: index+3]] == 'Stop':
                break
          if 'Stop' in protein and protein.replace('Stop', '') not in proteins[entry]:
            # print(f'''{dna_string} -> {protein.replace('Stop', '')}''')
            proteins[entry].append(protein.replace('Stop', ''))
    [print(protein) for protein in proteins[entry]]
      


# Need to check reverse.

translate_orf(entries)
