
my_dic1 = {}
my_dic2 = {"127.0.0.1": "로컬호스트", "168.126.63.1": "dns ip"}

print(my_dic2["168.126.63.1"])
print(my_dic2["127.0.0.1"])


# dictionary 값 추가
my_dic2["168.126.63.5"] = "dns 5"
print(my_dic2)
