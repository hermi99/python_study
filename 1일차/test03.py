
# function 정의
def print_age(age):

	# if문 연습(if ~ elif ~ else)
    if age >= 10 and age < 20: 
        print("10대 입니다.")
    elif age >= 20 and age < 30:
        print("20대 입니다.")
    else:
        print("30대 이상입니다.")

age = 25

# function 호출
print_age(age)

# function 호출시 값을 직접 전달
print_age(43)




### for 문 ###

# range(5) => [0, 1, 2, 3, 4]
# 배열의 값을 반복하면서 x라는 변수에 저장
for x in range(5):
    print(x)

list = [1, 3, 5, 7, 9]
for x in list:
    print(x)









