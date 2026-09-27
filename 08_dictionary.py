
# key : value
# d = { 1:"indore", "A":55, "goa": 15.5 }

# print(d)    # {1: 'indore', 'A': 55, 'goa': 15.5}
# print(d[1]) # indore
# print(d["goa"]) # 15.5

# print(type(d))  # <class 'dict'>

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(car) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# print(len(car)) # 3

# dct = dict(name= 'Mohan', age = 26)
# print(dct) # {'name': 'Mohan', 'age': 26}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# x = thisdict["model"]
# print(x) # Mustang

# x= thisdict.get('model')
# print(x)  # Mustang

# x = thisdict.keys()

# print(x)    # dict_keys(['brand', 'model', 'year'])

# print(thisdict.items()) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# print(thisdict.values()) # dict_values(['Ford', 'Mustang', 1964])

# thisdict['color'] = 'Red'

# print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'Red'}

# thisdict["model"] = 'xuv'

# print(thisdict) #{'brand': 'Ford', 'model': 'xuv', 'year': 1964}

# thisdict.update({'model': 'New XUV'})

# print(thisdict) # {'brand': 'Ford', 'model': 'New XUV', 'year': 1964}

# thisdict.update({'color':'red'})

# print(thisdict) # {'brand': 'Ford', 'model': 'New XUV', 'year': 1964, 'color': 'red'}

# thisdict.pop('model')
# print(thisdict) #{'brand': 'Ford', 'year': 1964, 'color': 'red'}

# thisdict.popitem()

# print(thisdict) #{'brand': 'Ford', 'year': 1964}

dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

# print(dict) # {'a': 'alpha', 'g': 'gamma', 'o': 'omega'}

# for key in dict:
#   print(key) 
#   # o/p- a
#   #g
#   #o
  
# for key in dict.keys():
#   print(key)  # it will print keys same as above
  
# for key in sorted(dict.keys()):
#   print(key, dict[key]) # each key/value will printed in key based sorted-order 
#   # a alpha
#   # g gamma
#   # o omega
  
# for value in dict.values():
#   print(value)  # it will print values of each key
  
dict1 = {
  'a':1,
  'e':7,
  'k':10,
}

dict2= dict1
# print(dict2) # {'a': 1, 'e': 7, 'k': 10}

# dict1.update({'o':77})
# print(dict1) # {'a': 1, 'e': 7, 'k': 10, 'o': 77}
# print(dict2) # {'a': 1, 'e': 7, 'k': 10, 'o': 77}

# copy() method 
# copied_dict = dict1.copy()  # {'a': 1, 'e': 7, 'k': 10}

# print(copied_dict)

# dict1['120'] = 'bcnjqni' # change will not reflect to copied_dict 

# print(dict1) # {'a': 1, 'e': 7, 'k': 10, '120': 'bcnjqni'}
# print(copied_dict) # {'a': 1, 'e': 7, 'k': 10}


##### Nested dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily) # {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
  
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
        
        
        ###--- output
#         child1
# name: Emil
# year: 2004
# child2
# name: Tobias
# year: 2007
# child3
# name: Linus
# year: 2011