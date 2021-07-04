with open('rosalind_iev.txt', 'r') as txt_obj:
  crosses = {'AA-AA':{'Num': 0, 'Dom_%':1}, 
  'AA-Aa':{'Num': 0, 'Dom_%':1}, 
  'AA-aa':{'Num': 0, 'Dom_%':1}, 
  'Aa-Aa':{'Num': 0, 'Dom_%':0.75}, 
  'Aa-aa':{'Num': 0, 'Dom_%':0.5},
  'aa-aa':{'Num': 0, 'Dom_%':0}}
  for pair, num, in zip(crosses.values(), txt_obj.read().split()):
    pair['Num'] += int(num)

dom_phenotypes = [values['Dom_%'] * values['Num'] for values in crosses.values()]
print(sum(dom_phenotypes) * 2)