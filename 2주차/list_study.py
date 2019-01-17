
# list
my_list1 = []
my_list2 = [1, 2, 3, 4, 5]

print(my_list1)
print(my_list2)

for data in my_list2:
    print(data)

sum = 0
for data in my_list2:
    sum += data

print("sum[1-5]:", sum)


#list에 값추가
my_list1.append("jugnil1")
my_list1.append("jugnil2")
my_list1.append("jugnil3")
print(my_list1)

print(my_list2[2])
print(my_list2[2:4])

del(my_list2[2])
print(my_list2)

print("list 길이:", len(my_list2))









