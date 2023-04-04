set_countries = {'col', 'mex', 'bol'}
"""
print(len(set_countries))
print('col' in set_countries)
"""
#add
set_countries.add('pe')
print("Is Peru ad countries set?")
print('pe' in set_countries)
print(set_countries)

#update
set_countries.update({'arg','ven','chi'})
print(set_countries)

#remove
set_countries.remove('col')
set_countries.discard('mex')
print(set_countries)