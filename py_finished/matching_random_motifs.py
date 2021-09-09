import functools
import operator

N = 87018 # Number of strings
x = 0.552333 # GC Content
s = list('CTATAACTTC')
nt_perc = {'G': x/2, 'C': x/2, 'A': (1-x)/2, 'T':(1-x)/2}

P = functools.reduce(operator.mul, [nt_perc[nt] for nt in s])
# Probability of motif.

print(round(1-(1-P)** N, 5))
# (1-P)**N - Probability of the string never appearing.

# Ugh. Why am I so bad at this. I thought that using the binomial dist would be the right move.
# IT CLEARLY MENTIONS COMPLEMENT. 
# Just 1 - P(Ac) (No occurence of string.)
