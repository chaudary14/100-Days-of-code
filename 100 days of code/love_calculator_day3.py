print("WELCOME TO LOVE CALCULATOR!")
name1 = input("What is your name? \n").lower()
name2 = input("What is your name? \n").lower()


combined = str(name1) + str(name2)


t = combined.count("t")
r = combined.count("r")
u = combined.count("u")
e = combined.count("e")

true = t + r +u +e
# if "t" in name1 or name2:
    # t= name1.count("t") + name2.count("t")
# if "r" in name1 or name2:
    # r= name1.count("r") + name2.count("r")
# if "u" in name1 or name2:
    # u= name1.count("u") + name2.count("u")
# if "e" in name1 or name2:
    # e= name1.count("e") + name2.count("e")

# total1 = int(t) + int(r) +int(u) + int(e)
l = combined.count("l")
o = combined.count("o")
v = combined.count("v")
e = combined.count("e")

love = l + o +v +e

# if "l" in name1 or name2:
#     l= name1.count("l") + name2.count("l")
# if "o" in name1 or name2:
#     o= name1.count("o") + name2.count("o")
# if "v" in name1 or name2:
#     v= name1.count("v") + name2.count("v")
# if "e" in name1 or name2:
#     e= name1.count("e") + name2.count("e")

# total2 = int(l) + int(o) +int(v) + int(e)


# final_score = str(true) +str(love)
# easy method
final_score = int(str(true) + str(love))

if final_score > 90 or final_score < 10:
    print(f"Your score is {final_score}, you go like coke and mentos")
elif final_score> 40 and final_score < 50:
    print(f"YOur score is {final_score},you are alright together")
else:
    print(f"your score is {final_score}")







"""
name1 =(name1.lower())
name2 =(name2.lower())


t1= name1.count("t")
t2= name2.count("t")
t = int(t1)+int(t2)
print("total t count is:", int(t1)+int(t2))
r1 =name1.count("r")
r2 =name2.count("r")
r = int(r1)+int(r2)
print("total r count is:", int(r1)+int(r2))
u1 =name1.count("u")
u2 =name2.count("u")
u = int(u1)+int(u2)
print("total u count is:", int(u1)+int(u2))
e1 =name1.count("e")
e2= name2.count("e")
e = int(e1)+int(e2)
print("total t count is:", int(e1)+int(e2))

x = t + r + u + e


l1 =name1.count("l")
l2 = name2.count("l")
l =int(l1) +int(l2)
o1=name1.count("o")
o2=name2.count("o")
o = int(o1)+int(o2)
v1=name1.count("v")
v2=name2.count("v")
v = int(v1) +int(v2)
e1 =name1.count("e")
e2 =name2.count("e")
e = int(e1) + int(e2)

y = l +o + v + e

z = str(x) + str(y)
print(z)

"""