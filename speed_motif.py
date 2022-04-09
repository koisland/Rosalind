# C A G C A T G G T A T - C A C A G C A G A G
# 0 0 0 1 2 0 0 0 0 0 0 - 1 2 1 2 3 4 5 3 0 0

# Rosalind Ex
# Looking for ACGTACGT
# T A G G T A C G T A  C  G  G  C  A  T  C  A  C  G
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

from rosalind_resources import unpack_fasta

s = list(unpack_fasta('rosalind_kmp.txt').values())[0]


def fail_array(seq):
    motif = {}
    motif_pos = 1
    seq_pos = 1
    f_array = []
    found_motif = False
    for nt in seq[:]:
        if nt == motif.get(seq_pos):
            f_array.append(seq_pos)
            seq_pos += 1
            found_motif = True
        elif nt != motif.get(seq_pos) and not found_motif:
            f_array.append(0)
            motif[motif_pos] = nt
            motif_pos += 1
        elif nt == motif.get(1):
            f_array.append(1)
            seq_pos = 2
        else:
            f_array.append(0)
            seq_pos = 1
    return f_array


print(' '.join(list(s)))
print(' '.join(map(str, fail_array(s))))
