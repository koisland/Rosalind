import time
from rosalind_resources import unpack_fasta

substrings = list(unpack_fasta('rosalind_long.txt').values())

superstring = substrings[0] # Start with first substring.
# Should be 'ATTAGACCTGCCGGAATAC' in the order of substrings 1, 3, 2, and 4 

# print(substrings)

done = False
total_time = 0
while not done:
  start_time = time.time()
  for substr in substrings[1:]:
    # print('Searching through: ', substr)
    for pos, nt in enumerate(substr):
      trail_seg = substr[:-pos]
      lead_seg = substr[pos:]
      if lead_seg in superstring and substr in substrings and len(lead_seg) > (len(substr)/2):
        # print(segment, substr[-pos:])
        superstring = substr[:pos] + superstring
        substrings.remove(substr)
      elif trail_seg in superstring and substr in substrings and len(trail_seg) > (len(substr)/2):
        superstring += substr[-pos:]
        substrings.remove(substr)
        # print(substrings)
        # print(superstring)
        # NEED to find way to check leading end in addition to  the trailing end.
  end_time = time.time()
  total_time += end_time-start_time
  print(round(total_time, 3))
  print(f'Strings left: {len(substrings)}')
  if len(substrings) == 1:
    done = True

# Suboptimal code. Takes a minute to output result.

print(superstring)
