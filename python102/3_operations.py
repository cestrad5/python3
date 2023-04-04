set_a= {1,2,3,4}
set_b= {4,5,6}

#union 
#set_c= set_a | set_b
set_c = set_a.union(set_b)
print(set_c)

#Intersection
set_d= set_a.intersection(set_b)
print(set_d)
print(set_a & set_b)

#difference
sed_e= set_a.difference(set_b)
print(sed_e)
print(set_a - set_b)

#symmetry difference
set_f = set_a.symmetric_difference(set_b)
print(set_f)
print(set_a ^ set_b)