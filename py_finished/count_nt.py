s = "GAGTCGCGGGCCTACGTTTAGTCGGTCTTGATATTCTGACCCGAGCTGTTATTTGTAGTCGTGTTGTAATAGAATGCTGACCACCAAGGAACAGATACTTCATTAATTGCGGACGCTTTTAGCCCCAAGACTGAGTTTATCGGCGCGTTGTACCGGACCGGTACCGCCATCTAGAAACTTACGAAGCGGAATCTCCCCGACATCTCGCAAGAAGATCCCGGACCGTGTCGTATGAGTCGTCCCGGCTGAACTGCCCGGCACTCGAAACTCGCCTTCTAGGGCGAGACGAAACTCGCTTGCGGATAGAAGCAACTACAGAGGCTTTGTTCGTGTTTGCGACCAGACCCAGACGGCTTGACTATGGAATCTCACTGGCTGCCGCTATGGCCGGCGCCAGGCAAACATTCACCCGATAAGCGACCGTCCCTACTAAACAGGGTCTAGGCTAGTAGCTCGCCGGGGCAAACATGCCAAATTTAACTTGTTACTTCGAGTCTAGATTTACAATTATAGCACTTGAGAACGGGATGATGGTAGCGGCCCTGCCCCTAGTGTTGAGAACTGGGGCCTCAAAAACTAGGTCCTCTCGTTTTTGGTTAACGTTGTGAACAATTGCGCAAAATATGATGCCATCGATACACCAACAGACCAGCATGGGACAGGCAGTCTGAGTCAGCTGGTGGTGGTCTGCTTGCTCATAACTTGCCCAAAACGCATAAGGATATGACAATCTATGTCTGAATCATGTAGCAATAAGCCCTAACTCTTCGACGCCGCCCCGCACCCGGTATTATGTGGCCTATAGACGAACCTTAGTGAAGTTAACAACGCAAGCTTAGACGTTTACGGTAAACTACCTCGACGGGCTAGCTTCTTAGGCCTCTGAAACATGCTTGTCCCTATTTGAGTTTACGACGCATCTGGGCGGTCCCTGCCTTCGACCGATGTCCCTGCTCCCGATGTCT"
A = 0
T = 0
G = 0
C = 0
list = [A, C, G, T]
for x in s:
  if x == "A":
    list[0] += 1
  elif x == "C":
    list[1] += 1
  elif x == "G":
    list[2] += 1
  elif x == "T":
    list[3] += 1
  else:
    print("what planet are you from?")
print (list)

