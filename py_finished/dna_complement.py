file = open('rosalind_revc.txt', 'r')
seqstring = file.read()
s = list(seqstring)
sc = []

for x in s:
    if x == "A":
        sc += "T"
    elif x == "T":
        sc += "A"
    elif x == "G":
        sc += "C"
    elif x == "C":
        sc+= "G"

seq = ''.join(map(str,sc))
cseq = seq[::-1]
print (cseq)


