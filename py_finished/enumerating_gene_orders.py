# import math                                         
# import itertools  

# n = 6                                               
# print(math.factorial(n))                            
# perm = itertools.permutations(list(range(1, n + 1)))

# [print(str(item).strip('()').replace(',', ' ')) for item in list(perm)]

# From 'Sara does Bioinformatics'. 
# I should really look into relevant libraries before trying to code it myself...


def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
                
# From ActiveState Code Recipes
print(list(all_perms([1, 2, 3])))
