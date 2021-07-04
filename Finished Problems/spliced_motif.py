from rosalind_resources import unpack_fasta

strings = list(unpack_fasta('rosalind_sseq.txt').values())

subseq_ind = ['0']
for subseq_nt in strings[1]:
  for ind, nt in enumerate(strings[0], 1):
    if nt == subseq_nt and ind > int(subseq_ind[-1]) + 1:
      subseq_ind.append(str(ind))
      break

print(' '.join(subseq_ind[1:]))