
my_set= {12,52,14,5,1,4,12,4} # duplicates will be removed by set

# print(my_set) #{1, 4, 5, 52, 12, 14}
# s1 = set()
# s2={}
# print(type(s1)) #<class 'set'>
# print (type(s2)) #<class 'dict'>

# s3 = set(range(4,9))
# print(s3) #{4, 5, 6, 7, 8}

basket = {10,2,4.210,19,True,22,'Melodi', 5, 'Neha'}

# print('neha' in basket) # False
# print('Neha' in basket) # True 

# print(4.210 in basket) # True

# print(4.211 in basket) # False

# print(basket[2]) #TypeError: 'set' object is not subscriptable


# fruits_Set = {"apple", "banana", "cherry"}
# print(fruits_Set)           # {'cherry', 'apple', 'banana'}
# fruits_Set.add('Orange')    
# print(fruits_Set)           # {'cherry', 'apple', 'Orange', 'banana'}

# fruits_Set_2 = {'Mango', 'Papaya'}

# fruits_Set.update(fruits_Set_2)

# print(fruits_Set)   # {'cherry', 'Orange', 'Papaya', 'apple', 'Mango', 'banana'}

st1 = {'a','b','c'}

# print(st1) # {'a','b','c'}

# st1.remove('b')
# print(st1) # {'a','c'}

# st1.discard('c')
# print(st1)

# st1.remove('bob') # KeyError: 'bob'
# st1.discard('bob') # It will not return any error

# st1.pop()
# print(st1) # set()


# s_clear = {5,9,2,7}

# s_clear.clear() 
# print(s_clear)  # set()

# s_del = {2,5,1}

# del s_del  # s_del will be deleted =. hence trying acceing it will throw error
# print(s_del)  # NameError: name 's_del' is not defined

# for b in basket:
#     print(b)

# i=0
# l= list(basket)
# while i < len(l):
#     print(l[i])
#     i+=1

set1= {1,2,3,4,6,False}
set2 = {2,5,1,9,7}
t1 = (1.2, 4.9, 3.2819)
s0 ={'a'}

# set3 = set1.union(set2)
# set4= set1 | set2
# print(set3) # {1, 2, 3, 4, 5, 6, 7, 9}
# print(set4) #{1, 2, 3, 4, 5, 6, 7, 9}

# print(set1.union(set1,set2,s0)) # {False, 1, 2, 3, 4, 5, 6, 7, 9, 'a'}

# print(set1 | set2 | s0) #{False, 1, 2, 3, 4, 5, 6, 7, 9, 'a'}

# print(set1.union(t1)) # {False, 1, 2, 3, 4, 1.2, 6, 4.9, 3.2819}

# print( set1 | t1) #TypeError: unsupported operand type(s) for |: 'set' and 'tuple'

# set1.update(set2)
# print(set1) #{False, 1, 2, 3, 4, 5, 6, 7, 9}

a = set('abrpcdq')
b = set('alanbz')

# print(a.intersection(b)) # {'b', 'a'}
# print(a & b) # {'b', 'a'}

# print(a.difference(b)) # {'p', 'q', 'c', 'r', 'd'}
# print(a - b) # {'p', 'q', 'c', 'r', 'd'}

# print(a.symmetric_difference(b))  # {'q', 'c', 'd', 'l', 'n', 'z', 'p', 'r'}
# print(a ^ b) # {'q', 'c', 'd', 'l', 'n', 'z', 'p', 'r'}

# ==========================================
# FROZENSET & IT'S ALL METHODS
# ==========================================


# f = frozenset({12, 2,5,9, 1, 2, 9, 21})
# print(f) #frozenset({1, 2, 5, 21, 9, 12})

# a = frozenset({1, 2, 3})
# b = frozenset({3, 4, 5})

# print(a.union(b))
# # frozenset({1, 2, 3, 4, 5})


a = frozenset({"a", "b", "c", "d"})
b = frozenset({"c", "d", "e", "f"})


# 1. copy()
print(a.copy())
# frozenset({'a', 'b', 'c', 'd'})


# 2. union()
print(a.union(b))
# frozenset({'a', 'b', 'c', 'd', 'e', 'f'})

print(a | b)
# frozenset({'a', 'b', 'c', 'd', 'e', 'f'})


# 3. intersection()
print(a.intersection(b))
# frozenset({'c', 'd'})

print(a & b)
# frozenset({'c', 'd'})


# 4. difference()
print(a.difference(b))
# frozenset({'a', 'b'})

print(a - b)
# frozenset({'a', 'b'})


# 5. symmetric_difference()
print(a.symmetric_difference(b))
# frozenset({'a', 'b', 'e', 'f'})

print(a ^ b)
# frozenset({'a', 'b', 'e', 'f'})


# 6. isdisjoint()
c = frozenset({"x", "y", "z"})

print(a.isdisjoint(c))
# True

print(a.isdisjoint(b))
# False


# 7. issubset()
d = frozenset({"a", "b"})

print(d.issubset(a))
# True

print(d <= a)
# True

print(d < a)
# True


# 8. issuperset()
print(a.issuperset(d))
# True

print(a >= d)
# True

print(a > d)
# True


# ==========================================
# BUILT-IN FUNCTIONS
# ==========================================

# 9. len()
print(len(a))
# 4


# 10. min()
numbers = frozenset({12, 2, 5, 9, 1, 21})

print(min(numbers))
# 1


# 11. max()
print(max(numbers))
# 21


# 12. sum()
print(sum(numbers))
# 50


# 13. sorted()
print(sorted(numbers))
# [1, 2, 5, 9, 12, 21]


# 14. membership - in
print("a" in a)
# True


# 15. membership - not in
print("z" not in a)
# True


# ==========================================
# OPERATORS
# ==========================================

# Union
print(a | b)
# frozenset({'a', 'b', 'c', 'd', 'e', 'f'})


# Intersection
print(a & b)
# frozenset({'c', 'd'})


# Difference
print(a - b)
# frozenset({'a', 'b'})


# Symmetric difference
print(a ^ b)
# frozenset({'a', 'b', 'e', 'f'})


# Subset
print(d <= a)
# True


# Strict subset
print(d < a)
# True


# Superset
print(a >= d)
# True


# Strict superset
print(a > d)
# True


# Equality
print(a == a)
# True


# Not equal
print(a != b)
# True