import re
import functools

def unpack_fasta(fasta_file):
  with open(fasta_file) as file_obj:
    entries = {}
    prev_entry = 0
    fasta_str = file_obj.read()
    for pos, char in enumerate(fasta_str):
      if char == '>' and pos != 0:
        entry = fasta_str[prev_entry:pos].split('\n', 1)
        entries[entry[0]] = entry[1].replace('\n', '')
        prev_entry = pos
    fin_entry = fasta_str[prev_entry:].split('\n', 1)  
    # Last > entry will not be added in if statement above. Add here ^^^.
    # Split only the first time it finds a newline.
    entries[fin_entry[0]] = fin_entry[1].replace('\n', '')
    return entries

def codons(na_type):  # RNA or DNA
  with open(f'{na_type} codon table.txt', 'r') as codons:
    raw_txt = codons.read()
    codon_dict = {}
    codons = re.findall('[A(T|U)GC]{3}', raw_txt)
    amino_acids = re.findall('(?<=\s)(\w|Stop)(?=\s)', raw_txt)
    for codon, aa in zip(codons, amino_acids):
        codon_dict[codon] = aa
    return codon_dict
  
def find_string(entries, str_type='shortest'):
  if type(entries) == dict:
    iterable = entries.values()
  else:
    iterable = entries
  if str_type == 'shortest':
    len_check = lambda str1, str2: len(str1) < len(str2)
  elif str_type == 'longest':
    len_check = lambda str1, str2: len(str1) > len(str2)
  result = functools.reduce(lambda x, y: x if len_check(x, y) else y, iterable)
  return result



