# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet)
# print(5 in cabinet)
 
cabinet = {"A-3": "유재석", "B-100":"김태호"}
#print(cabinet["A-3"])
#print(cabinet["B-100"])

#                                           새 손님 
#print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
#print(cabinet)

#                                           간 손님 
del cabinet["A-3"]
#print(cabinet)

#key 들만 출력
#print(cabinet.keys())

#value 들만 출력
#print(cabinet.values())

#key, value 쌍으로 출력 
#print(cabinet.items())

#                                           목욕탕 페점 
cabinet.clear
#print(cabinet)

##########################################################

# 튜플

menu = ["돈까스", "치즈까스"]
#print(menu[0])
#print(menu[1])

# name = "김종국"
# age = 20 
# hobby = "코딩"
# print(name,age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
#print(name, age, hobby)

############################################################

#집합 (set)
# 중복 안됨, 순서 없음 
my_set = {1,2,3,3,3}
#print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java 와 python 을 모두 할수 있는 개발자)
#print(java & python)
#print(java.intersection(python))

#합집합 (java 할 수 있거나 python 할수 있는 개발자)
#print(java | python)
#print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
#print(java - python)
#print(java.difference(python))

# python 할 줄 아는 사람이 늘어남 
python.add("김태호")
#print(python)

# java 를 잊었어요 
java.remove("김태호")
#print(java)

#######################################

#자료구조의 변경 

menu = {"커피", "우유", "주스"}
#print(menu, type(menu))

menu = list(menu)
#print(menu, type(menu))

menu = tuple(menu)
#print(menu, type(menu))

menu = set(menu)
#print(menu, type(menu))

########################################
# 퀴즈 4 (1:53:34)

# from random import *
# users = range(1, 21) 
# users = list(users)

# shuffle(users)
# print(users)

# winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
# print(" -- 당첨자 발표 -- ")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 -- ")

########################################

#for 

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# print("대기번호 : 5")

#for waiting_no in [1,2,3,4,5]:
#    print("대기번호 : {0}".format(waiting_no))

#for waiting_no in range(1, 6):
#    print("대기번호 : {0}".format(waiting_no))

#starbucks = ["Jae", "Jill", "Jack"]
#for customer in starbucks: 
#    print("{0}, 커피가 준비되었습니다.".format(customer))

#########################################

# while 

# customer = "토르"
# index = 5 
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1 
#     if index == 0:
#         print("커피는 페기처분되었습니다.")

# customer = "아이언맨"
# index = 0 
# while True: 
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1 

# customer = "토르"
# person = "Unknown"

# while person != customer: 
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

###############################################

#continue and break

# absent = [2, 5] #결석 
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11): 
#     if student in absent: 
#         continue 
#     elif student in no_book:
#         print("오늘 수없 여기까지, {0}는 교무실로 따라와".format(student))
#         break  
#     print("{0}, 책을 얽어봐".format(student))

################################################

# 한줄 for 
#출석번호 가 1,2,3,4 앞에 100을 붙이기로 함 -> 101,102,103,104

# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)

#학갱 이름을 길이로 번환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i)-1 for i in students]
print(students)