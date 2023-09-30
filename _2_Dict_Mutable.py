
# Dictionary is mutable
# int x = 10
# CREATE

'''
'''
'''
Keys must be unique and immutable
Value can be anything

Signup operation:
===================
FisrtName:  <Dyn data>
LastName :  <Dyn data>
Email    :  <Dyn data>
MobileNo :  <Dyn data>


'''
# CREATE
data = {1: 'One', 2: 'Two', 3: 'Two', 'id': '100'}

# RETRIEVE
print("Dictionary : ", data, type(data))
print("Dict item  :", data[2])
print("Dict item  :", data['id'])

# UPDATE
data[2] = 'Twenty'
data['id'] = 200
print("Dictionary update: ", data)

'''
# DELETE
=============
1. Delete entire  dict   --> del dict1
2. Delete any one item   --> del dict1['id']
3. Delete entire items   --> dict1.clear()
'''

del data[3]
del data['id']
print("Dictionary delete1: ", data)

data.clear()
print("Dictionary delete2: ", data)

data['sal'] = 1000
print("Dictionary delete3: ", data)

# del data
x = 10
print("X : ", x)
del x
# print("X : ",x)

del data
# print("Dictionary delete: ", data) ERROR
