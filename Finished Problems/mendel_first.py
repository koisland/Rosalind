ho_d = 16 # k AA
he = 21 # m Aa
ho_r = 22 # n aa
# Will have dominant allele.
pop_size = ho_d + ho_r + he

ho_r_ho_r = (ho_r / pop_size) * ((ho_r - 1) / (pop_size - 1)) 
ho_r_he = (((ho_r/pop_size) * (he / (pop_size - 1))) * 0.5)
he_he = ((he/pop_size) * ( ( (he - 1) / (pop_size - 1))) * 0.25)

perc_dom = 1 - (ho_r_ho_r + (2 * ho_r_he) + he_he)
# 1- ((ho_r x ho_r) + 2(ho_r x he)(0.5) + (he x he)(0.25))'
# Totally forgot that because ho_r OR he can be selected, must multiply by two. 
# :((((
# I am bad at statistics...
print(perc_dom)