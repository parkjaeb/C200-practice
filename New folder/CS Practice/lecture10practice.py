# #SLIDE 2-3

# def greeting(x):
#     return "Hello, " + x

# print(greeting("Earthling"))

# #SLIDE 4-5

# def greeting(x):
#         print("Hello,",x)

# greeting("friends")
# print(greeting("friends")) 

# #SLIDE 6-7

# def g(x):
#     return 2*(x**2)
# def f(x):
#     return x + 10

# print(f(g(4)))

# #SLIDE 8-9
# def y(a,r,x):
#     growth = a*(1 + r/100)**x
#     return growth

# population = 100000
# rate = 2
# years = 10
# print(y(population, rate, years))

# #SLIDE 10-11
# def foo(start,end,step):
#     return list(range(start,end,step))

# print(foo(0,5,2))

# SLIDE 12-13

# def foo(xlst):
#     cnt = 0
#     if xlst:
#         for i in xlst:
#             if i == 1:
#                 cnt += 1
#     return cnt

# x = [ [], [1,2,1], [2,3,4]]
# for i in x:
#     print(foo(i))

# #SLIDE 14-15
# def sort_candy(clist):
#     xtmp = []
#     for i in clist:
#         if 30 <= i and i <= 40:
#             xtmp += ["yes"]
#         else:
#             xtmp += ["no"]
#     return xtmp

# candy = [30,34,45,30]
# print(sort_candy(candy))

# #SLIDE 16-17
# def x(xlst):
#     if xlst:
#         for i,j in enumerate(xlst):
#             xlst[i] = 8 - j
#     return xlst

# y = [1,8,-1,0,2]

# print(x(y))

# #SLIDE 19-21
# def x(xlst):
#     for i,j in enumerate(xlst):
#         screw,washer,bolt = 8-j[0], 4-j[1], 4-j[2]
#         xlst[i] = [screw, washer, bolt]
#     return xlst

# y = [[8,4,4],[9,3,4],[2,0,1]]

# print(x(y))

# ##SLIDE 21-22
# def occurs(x,xlst):
#     cnt = 0
#     if xlst:
#         for i in xlst:
#             cnt += 1*(i == x)
#     return cnt

# x1,x2,x3 = [1,2,1,2,3],[],[[],1,[2],[],3]
# xlst = [x1,x2]
# for i in xlst:
#     print(occurs(1,i))
   
# print(occurs([],x3))

# #SLIDE 23-24
# def remove_all(x,xlst):
#     xtmp = []
#     for i in xlst:
#         if not (x == i):
#             xtmp += [i]
#     return xtmp

# x = [1,2,1,1,2,1,23,3,1,3,1]

# print(remove_all(1,x))

# #SLIDE 25-26
# def checker(xlst):
#     correct = 0
#     for i in xlst:
#         x,op,y,answer = i
#         if (op == "*" and (x*y == answer)) or \
#            (op == "+" and (x+y == answer)) or \
#            (op == "-" and (x-y == answer)):
#             correct += 1

#     return correct
# x = [[4,"*",4,15], [2,"*",3,6],[1,"-",3,-2], [100,"+",1,101]]

# ans = checker(x)
# print("Correct:", ans)
# print("Incorrect:", abs(len(x)-ans))

# #SLIDE 28-29
# def add(x):
#     def g(y):
#         return x + y
#     return g

# f = add(3)
# print(f(4))

# SLIDE 29-30
# def foo(args):
#     x,y,z = args
#     if x <= y and y <= z:
#         return [x,y,z]
#     if x <= z and z <= y:
#         return [x,z,y] 
#     if y <= x and x <= z:
#         return [y,x,z]
#     if y <= z and z <= x:
#         return [y,z,x] 
#     if z <= y and y <= x:
#         return [z,y,x]
#     if z <= x and x <= y:
#         return [z,x,y]   
    
# x = [(1,2,3),(1,3,2),(2,3,1),(2,1,3),(3,1,2),(3,2,1)]

# for i in x:
#     print(foo(i))

# SLIDE 35-36

# def ave(xlst):
#     sum = 0
#     for i in xlst:
#         sum += int(i)
#     return sum/len(xlst)

# n = input("Integers to average (csv) ")
# n = n.split(",")
# print(ave(n))

# #SLIDE 37-38

# def con_ar(verb):
#     stem = verb[0:len(verb)-2]
#     endings = ['o','as','a','amos','ais','an']
#     tlst = []
#     for i in endings:
#         tlst += [stem + i]
#     return tlst

# print(con_ar("hablar"))

# #SLIDE 39
# import random as rn

# def ave(xlst):
#     sum = 0
#     for i in xlst:
#         sum += i
#     return sum/len(xlst)

# def nearest(xlst,x):
#     start = xlst[0]
#     for i in xlst:
#         if abs(i - x) < abs(start - x):
#             start = i
#     return start

# size = rn.randint(1,5)
# xlst = []
# for i in range(size):
#     xlst += [rn.randint(1,100)]

# print(xlst)
# ave_ = ave(xlst)
# print(ave_)
# print(nearest(xlst, ave_))

# #SLIDE 41,42,43

# import random as rn

# site = (rn.randint(-50,50), rn.randint(-50,50))

# def direction(site):
#         x,y = site
#         x_dir = "W"*(x < 0) + "E"*(x > 0) + "S"*(x == 0)
#         y_dir = "N"*(y > 0) + "S"*(y < 0) + "S"*(y == 0)
#         return y_dir + x_dir

# print(site)
# print(direction(site))

# #SLIDE 44-45

# import random as rn

# def roll():
#     d1,d2 = rn.randint(1,6),rn.randint(1,6)
#     return d1 + d2

# cnt = 0
# for i in range(100):
#     if roll() == 7:
#         cnt += 1

# print("You rolled 7", cnt, "times")

# SLIDE 46,47

# import math

# car = 15 #mpg
# tank = 10 #g
# travel = car * tank
# distance = 1000
# print(math.ceil(distance/travel))