l = [1,2,3,4,5,6,7,8]

# new_list = [num * num for num in l ]

new_list2 = [ l2* l2 for l2 in l if l2 % 2 == 0 ]

# print(new_list)

print(new_list2)

names = ["gopi", "rahul", "arun", "dhinesh"]

new_name = [n.upper() for n in names]

print(new_name)