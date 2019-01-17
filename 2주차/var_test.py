

#string
#int
#float
#Bolean : True/False

name = "jungil"
count = 5
temp = 5.5
active = True

print(name)
print(count)
print(temp)
print(active)

name = "jungil2"
print(name)


print("name :", name)
print("name :{}".format(name))
print("name :{}, count:{}".format(name, count))

if name == "jungil":
    print("hello ", name)
elif name == "xxx":
    print("print xxx")
else:
    print("who ?")


def print_var(name2, count2):
    print("name :", name2)
    print("name :{}".format(name2))
    print("name :{}, count:{}".format(name2, count2))

print("\nfunction print:")
print_var("jungil", 5)
print_var(name, count)














