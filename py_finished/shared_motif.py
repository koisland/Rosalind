from rosalind_resources import unpack_fasta, find_string

entries = unpack_fasta('rosalind_lcsm.txt')
# print(entries)

main_str = find_string(entries, str_type='shortest')

substr = []
longest_str = ''

for pos in range(0, len(main_str) + 1):
  main_slice = main_str[0:pos]
  if main_slice not in substr and main_slice != '':
      substr.append(main_slice)

def sub_str_check(sub_str, longest_str):
  if all(sub_str in entry for entry in entries.values()) and len(sub_str) > len(longest_str):
      return sub_str
      # check if str is longer than the the length of the next sub_str. then break
  else:
    return longest_str

# Go through all possible inner sub str in the longest sub str.
test_str = substr[-1]
# print(test_str)

for pos in range(len(test_str), 1, -1):

  if len(longest_str) >= pos:
    break
  longest_str = sub_str_check(test_str[pos:], longest_str)
  for in_pos in range(pos, 0, -1):
      sub_slice = test_str[in_pos:pos]
      if len(longest_str) >= in_pos:
        break
      longest_str = sub_str_check(sub_slice, longest_str)

print(longest_str)


# GAATTTGAGAAGCGCATTATGCGCATAGAGGGCTATGCATATGGCCGTGAACACTGTCCCTCACCACATCAATAAAGTTTGCCAGTCCCATTCACAGGCCGTACGTGACTCACATGCGGAACTGCACGAAACGCTCAGCGAACGTGAAGTTGTAACTACGTCGATGCTAACTGTGCACACGGGTGAATTACGTTTACTTGAGCTTCTGC
