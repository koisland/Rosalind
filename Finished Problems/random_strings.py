import math

dna_string = 'GTATAAGGAGGGAGGAAATGTACCCAGTAGAAGCTTAATTTCCCTTCGCTAAAAAAACCTAATCTTGCATAATTGGCATTTAGAGCTGTCAT'
gc_content_str = '0.124 0.134 0.249 0.281 0.354 0.400 0.439 0.549 0.579 0.668 0.706 0.799 0.816 0.892'

gc_array = gc_content_str.split(' ')

log_array = []

for perc in gc_array:
  a_t_perc = (1 - float(perc)) / 2
  g_c_perc = float(perc) / 2
  perc_match = 1
  for nt in dna_string:
    if nt == 'A' or nt == 'T':
      perc_match *= a_t_perc
    else:
      perc_match *= g_c_perc
  log_array.append(round(math.log10(perc_match), 3))

print(str(log_array).strip('[]').replace(',', ''))
