import math      
                                                              
k = 6         
# Number of generations.                                                                 
N = 17                    
# Number of AaBbs                                                    
P = 2**k                 
# Total population in family tree. Each generation yields two offspring hence the exponential.                                                  
probability = 0                                                                
for i in range(N, P + 1):                                                      
    prob = (math.factorial(P) /                                                
            (math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(
                P - i))      
    # Binomial distribution for single event. The range for loop goes through each individual in the population.                                       
    # Could also swap for combined binomial distribution.
    probability += prob     
    # Each is added to the overall 'probability'. The 'prob' decreases with each subsequent event.                                                   
print(probability)          

# Taken from Sara does Bioinformatics but annotated by me to help understand.
# Couldn't figure this one out on my own. 
# I also misread the question and thought that it was asking for the probability of AaBb in the final generation not the entire tree.