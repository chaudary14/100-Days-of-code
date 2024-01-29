dic = {
    "Bug":"an error which occurs in execution of the program "
}
# adding item to the dictionary
dic["loops"]= "to rrepeat steps agaon"
print(dic)
# editing item in dictionary

dic["loops"]= "editing the loops"
print(dic)

# emtying the dictionary
# dic = {}
# print(dic)

# looping throug dictionary
for key in dic:
    # it only prints key of the dictionary and not values of it
    print(key)
    # method to loop troug the values of key
    print(dic[key])