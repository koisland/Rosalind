file = open('', 'r')
seq = file.read()
rt = list(seq)

#DNA string with nt length at most 1000 nt

for x in rt:
    if x == "A":
        rt[rt.index(x)] = "A"
    elif x =="C":
        rt[rt.index(x)] = "C"
    elif x =="G":
        rt[rt.index(x)] = "G"
    elif x == "T":
        rt[rt.index(x)] = "U"

print(''.join(map(str,rt)))


