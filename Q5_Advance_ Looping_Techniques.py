# Task 1: Ice Cream BO-GO

ice_cream= ['vanilla', 'chocolate', 'strawberry','cookie dough','rum raisin']

# for flavor_1 in ice_cream:
#     for flavor_2 in ice_cream:
#         print(flavor_1, flavor_2)


# Task 2: Double UP! 

# for flavor_1 in ice_cream:
#     for flavor_2 in ice_cream:
#         if flavor_1 == flavor_2:
#             print("Double", flavor_1)
#         else:
#          print(flavor_1, flavor_2)
        
# Task 3: No Repeats! 

for flavor_1 in ice_cream:
    for flavor_2 in ice_cream:
        if flavor_1 == flavor_2:
            print("Double", flavor_1)
        else:
         print(flavor_1, flavor_2)
    for flavor_2 in ice_cream:
       ice_cream.remove (flavor_1)