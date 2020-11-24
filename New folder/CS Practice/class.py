# #                                                                               Learn Quiz 4 Breakout 1 
# #import math

# def photo(t):
#     return 100*(math.exp(-0.02*t)-math.exp(-0.1*t))

# #  print(photo(19))
# #  print(photo(20))
# #  print(photo(21))

# #                                                                                     Breakout 2 
# def temp(D):
#      return (100-(D/3))*(D**3)

# # print(temp(1.01))

# # int problem 
# def days(year):
#      return year * 364

# # age = int(input("How old are you in years? "))
# # print("You are", days(age), "days old more or less.")

# #                                                                               Learn Quiz 5 Breakout 1

# def FtoC(deg_f):
#      return (deg_f - 32)*(5/9)

# def CtoK(deg_c):
#      return deg_c + 273.15

# def FtoK(deg_f):
#      return CtoK(FtoC(deg_f))

# temp_F = -50
# temp_K = round(FtoK(temp_F) ,2)
# # print(temp_F, "deg Fahrenheit is", temp_K, "deg Kelvin")

# #                                                                                 ^^ Def within Def 
# def ftok(deg_f):   
#     def ftoc(deg_f):
#          return (deg_f - 32)*(5/9)
#     def ctok(deg_c):
#          return deg_c + 273.15
#          return ctok(ftoc(deg_f))

# temp_f = -50
# #temp_k = round(ftok(temp_f), 2)
# # print(temp_f, "deg Fahrenheit is", temp_k, "deg Kelvin")

# #                                                                                      Breakout 2 
# #import math 

# def s2(Hemo,B,A):
#     c = math.e**(-Hemo*B)
#     c = c*Hemo*A
#     return c
# # print(s2(.30,1,2))

# #                                                                           Learning Quiz 6 Breakout 1 
# def vending(nq,nd,nn):
#     total = nq *.25 + nd * .10 + nn * .05
#     cost = 1.75
#     if total >= cost:
#         return "Have a nice day! change:$" + str(round(total - cost,2))
#     else:
#         return "You need more change:$" + str(round(cost - total,2))
# nq = 6
# nd = 2
# nn = 2
# #print(vending(nq,nd,nn))

# nq = 1
# nd = 2
# nn = 2
# # print(vending(nq,nd,nn))
# #                                                                              Breakout 2 
# x = 1
# y = 2
# a = 3
# g = 4
# def f(x,y):
# #    print(a)
#  f(a+x,g+2)

# #                                                                              Week 4 (7)
# w = [10,9]
# x = [1,["dog", [w,3.1415], "dog"],4]
# y = [x[1][0],x[1][2]]
# w = [x[0],x[1][1],x[2]]
# # print(y)
# # print(w)


# x = "hello"
# z = list(x)
# z[0] = 'b'
# "".join(z)
# # print(z)


# start = 0
# bound = 10
# for i in range(start,bound):
# #     print(i)

#     y = ["x", x]
#     z = [y,3,[1,2,3]]
# #print(y)
# #print(z)

# x = ["happy", "joy", "glee", "good"]
# for i,j in enumerate(x):
# #     print(i,j, j[i])

# #                                                           Lecture 8 (Bounded and different methods)

#     x = ["cat","dog", [1,2], 24, (2,3,1)]
# #iterate over container 
# for i in x:
# #     print(i)
# #iterate over index into container
#     for i in range(len(x)):
# #     print(x[i])
# #iterate over idex AND container 
#      for i,j in enumerate(x):
# #     print(i,j)
#         cnt = 0 
# for i in x:
#     if cnt ==2:
#         break
#     cnt = cnt + 1
#     #print(i)

# #print(i)

# def even(x):
#     return bool(x % 2 == 0)

# def odd(x):
#     return not even(x)

# found = False

# x = [2,4,6,5,2]
# for i,j in enumerate(x):
#     if odd(j):
#          found = True
# #         print("Found odd number", j)


# #if not found:
# #    print("Didn't find odd number")

# ##############################################
# #     x = [100, 24, 4, 3]

# # joy = int(input("Enter integer: "))

# # found = False 

# # for i,j in enumerate(x):
# #     if i == joy:
# #         found = True 
# #         print(joy, "is in the list!")
# #     break
# # if not found:
# #     print(joy, "It is not in the list!")

# #                                                                            Lecture 9 (Unit Testing)
# # Finding smallest value 
# # def smallest(x,y):
# #     if x > y: 
# #         return y 
# #     else :
# #         return x 
# # print(smallest(1,2))
# # print(smallest(5,2))

# # x = [100,2,33,3]
# # smallest = x[0]

# # for i,j in enumerate(x):
# #     if j < smallest:
# #         smallest = j 

# # print("The smallest number is", smallest)

# #############################################

# #Random function and finding the min"
# # import random as rn 

# # size = rn.randint(0,5)
# # xlst = []
# # for i in range(size):
# #     xlst = xlst + [rn.randint(0,10)]

# # def min_list(xlst):
# #     smallest = []
# #     if xlst:
# #         smallest = xlst[0]
# #         for i in xlst:
# #             if i < smallest:
# #                 i = smallest
# #     return smallest

# # print("orignial list", xlst)
# # print("smallest number", min_list(xlst))

# ##############################################

# #Two bounded loops 
# # x = ["A", "B", "C"]
# # y = [1,2,3]
# # for i in x:
# #     for j in y:
# #         print(i,j)
# #         if i == "B" and j == 2:
# #             print("Your seat is {0}{1}!".format(i,j))

# ###############################################

# #Two bounded loops 
# # import random as rn 
# # x = (rn.randint(0,3), rn.randint(0,3)) #tuple 

# # print("The secret pair is", x)

# # for i in range(0,4):
# #     for j in range(0,4):
# #         if (i,j) == x:
# #             print("Found it", x)

# ################################################

# # import random as rn

# # def cnt_votes(xlst):
# #     yes,no = 0,0
# #     for i in xlst:
# #         if i == 1:
# #             yes += 1 #yes = yes + 1
# #         else: 
# #             no += 1
# #     return yes, no #tuple

# # number_votes = rn.randint(1,5)
# # votes = []
# # for i in range(number_votes):
# #     votes.append(rn.randint(0,1))

# # print(votes)
# # tally = cnt_votes(votes)
# # print("Yes:",tally[0])
# # print("No:", tally[1])

# #########################################

# # def replace(old,new,xlst):
# #     xtmp = []
# #     for i in xlst:
# #         if i == old:
# #             xtmp += [new]
# #         else:
# #             xtmp += [i]
# #     return xtmp

# # x = ["dog", 1,2,3,1,2,300,"dog"]
# # y = ["dog", 1,2,3,4,300,400]

# # for i in y:
# #     print("\nReplacing {0} with '#'".format(i))
# #     print(replace(i,"#", x))

# ########################################

# #                                                                                   Lecture 10 
# #               Lecture 10 Practice

# #                                                                 Lecture 11(unbounded loops: While)
# # x = False 
# # while x:
# #     print("Hello World!")
# # print("Yaabadabado!")

# #########################################
# # for i in range(1,5,2):
# #     print(i)

# # i = 1   # Same thing as above 
# # while i < 5:
# #     print(i)
# #     i = i + 2

# #########################################
# # xlst = [1,2,2,4,1,5]

# # def remove_for_index(x,xlst):
# #     if xlst:
# #         tmp = []
# #         for i in range(0,len(xlst)):
# #             if xlst[i] != x:
# #                 tmp += [xlst[i]]
# #         return tmp

# # def remove_for_list(x,xlst):
# #     if xlst:
# #         tmp = []
# #         for i in xlst:
# #             if i != x:
# #                 tmp += [i]
# #         return tmp 

# # def remove_while_index(x,xlst):
# #     i = 0
# #     tmp = []
# #     while 0 <= i and i < len(xlst):
# #         if xlst[i] != x:
# #                 temp += [xlst[i]]
# #         i += 1
# #     return tmp

# ########################################

# # for duck in range(3,19,4):
# #     i = 3
# #     while duck < 19:
# #         print(duck)
# #         duck = duck + 4
# # print(duck)

# #########################################

# # x = [3,0,5,-1]
# # c = x[0]
# # for i in range(1,len(x),1):
# #     if c > x[i]: # 3 > 0, 0 > 5, 0 > 3,
# #         c = x[i]
# # print(c)

# ########################################

# # You must use a for-loop
# # def f(xlst, v):
# #     found = False
# #     if xlst: 
# #         for i in xlst:
# #             if i == v:
# #                 found = True
# #         return found 

# # print(f([1,4,2,1],0))
# # print(f([1,4,2,1],1))
# # print(f([1,4,2,1],[2]))
# # print(f([],1))

# ##You must use a while-loop
# # def f(xlst,v):
# #     xtemp = xlst
# #     found = False
# #     while xtemp and not found:
# #         if v == xtemp[0]:
# #             found = True
# #         xtemp = xtemp[1:]
# #     return found

# # print(f([1,4,2,1],0))
# # print(f([1,4,2,1],1))
# # print(f([1,4,2,1],[2]))
# # print(f([],1))

# #############################
# #returns the number of times v occurs in xlist
# # def cnt(xlist,v):
# #     c = 0 
# #     xtemp = xlist:
# #     while xtemp: 
# #         if v == xtemp[0]:
# #             c += 1 
# #         xtemp = xtemp[1:]
# #     return c

# ################################

# #Guessing Game 
# #We would use while loop here because we do not know how many tries it will take for the player to guess the number
# # import random 
# # x = random.randint(1,100)
# # g = int(input("Guess: 1-100: "))

# # while g != x:
# #     if g > x: 
# #         print("Too high!")
# #         g = int(input("Guess again "))
# #     else:
# #         print("Too low!")
# #         g = int(input("Guess again "))
# # print("Great Job!")

# #################################
# #                                                      Lecture 12 
# # for big in range(0,4,3):
# #     print("$", end="")
# # print()
# # print(big)
# # #While loop 

# # big = 0 
# # while big < 4:
# #     print("$", end="")
# #     big = big + 3 
# # print()
# # print(big-3)
# #########################################
# # i = 10
# # while i <= 22:
# #     print(":)", end="")
# #     i = i + 4

# # print()
# # #Changing while loop to for loop in range
# # for i in range(0,13,4):
# #     print(":)", end="")
# # print()
# ##########################################

# # smile = ":)"
# # x = ["):", ":)", "(:", ":)", "><"]
# # cnt = 0 
# # for j in x:
# #     if smile == j:
# #         cnt = cnt + 1
# # print("There are ", str(cnt), smile)

# # #While loop
# # xtemp = x
# # cnt = 0
# # while xtemp:
# #     if smile == xtemp[0]:
# #         cnt += 1
# #     xtemp = xtemp[1:]
# # print("There are ", str(cnt), smile)

# ##########################################

# #Dictionary 
# # x = {1:"no",2:"yes",3:"maybe"}
# # print("Current dictionary {0}.".format(x))
# # x[1] = "possibly"
# # del x[3]
# # print("Current dictionary {0}.".format(x))

# # x = {1:"no", 2:"yes", 3:"maybe"}
# # for k,v in x.items():
# #     print("The key is {0} and value is {1}".format(k,v))

# ############################################

# #                                                                       Lecture 13 
# # Anonymous Functions 
# # def f(x):
# #     return x*2

# # print(f(2))
# # print(lambda x: x*2,2)
# # g = lambda x: x*2

# # print(g(2))

# ########################################

# #Sorted : Insertion 
# # def insertion_sort(a):
# #     i = 1
# #     while i < len(a):
# #         j = i 
# #         while j > 0:
# #             if a[j] < a[j-1]:
# #                 a[j],a[j-1] = a[j-1],a[j]
# #             j -= 1
# #         i += 1
# #     return a

# # print("Sorted")
# # print(insertion_sort(a))

# #########################################

# #Sorted : Bubble Sort 
# # import random as rn 

# # test = []

# # for i in range(0,10):
# #     test.append(rn.randint(0,100))

# # print("Random")
# # print(test)

# # def bubble_sort(a):
# #     for i in range(len(a)):
# #         for j in range(len(a)-1):
# #             if a[j] > a[j+1]:
# #                 a[j],a[j+1] = a[j+1],a[j]
# #     return a

# # print("Sorted")
# # print(bubble_sort(test))

# #########################################

# #                                                           Lecture 14 
# #Recurtion 
# # import random as rn
# # x = rn.randint(1,24)
# # print("There are {0} doughnuts in the box.".format(x))

# # def Box(n):
# #     if n == 0:
# #         return 0
# #     else:
# #         return Box(n-1)+1
# # print("There are {0} doughnuts in the box.".format(Box(x)))

# ###########################################
# # #Factorial using While 
# # def fac1(n):
# #     p = 1
# #     while n > 0:
# #         p = p * n
# #         n -= 1
# #     return p

# # #Factorial using for
# # def fac2(n):
# #     p = 1
# #     for i in range(n,0,-1):
# #         p = p * i
# #     return p

# # for i in range(0,10):
# #     print("{0}! = {1} = {2}".format(i,fac1(i),fac2(i)))

# #############################################
# #Recursive Function
# # def fac(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * fac(n-1)

# ###############################################
# #                                           Lecture 13
# # def(n):
# #     if n == 0:
# #         return 1
# #     else: 
# #         return n * f(n-1)
# # print(f(5))

# ##########################################

# #                                           Lecture 16
# # def a(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return a(n-1)-n

# # print(a(3))

# # #Unbounded loop: Recursion
# # def a(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return a(n-1)-n
    
# # def af(n):
# #     sum = 1
# #     for i in range(n,0,-1):
# #         sum -= i
# #     return sum

# # for i in range(0,6):
# #     print(a(i),af(i))

# # #Tail recursive fashion
# # def at(n,v=1):
# #     if n == 0:
# #         return v
# #     else:
# #         return at(n-1, v-n)

# # print(at(3))

# ##################################
# #unbounded loop: Rresursion
# # def r(a,b,xlst):
# #     if xlst:
# #         v = xlst[0]
# #         if v != a:
# #             return [v] + r(a,b,xlst[1:])
# #         else:
# #             return [b] + r(a,b,xlst[1:])
# #     else:
# #         return []

# # print(r(1,2,[1,2,1]))

# #Unbounded loop: recursion to for loop
# # def rf(a,b,xlst):
# #     tmp = []
# #     for i in xlst:
# #         if i != a:
# #             tmp += [i]
# #         else:
# #             tmp += [b]
# #     return tmp 

# # print(rf(1,2,[1,2,1]))
# ############################################
# #Bottom-up 
# # d = {0:1,1:1}
# # def fac(n):
# #     if n in d.keys():
# #         return d[n]
# #     else:
# #         for i in range(2,n+1):
# #             d[i] = i*d[i-1]
# #         return d[n]

# # print(fac(5))
# # print(d)

# #Top-down
# # e = {0:1,1:1}
# # def fact(n):
# #     if n in e.keys():
# #         return e[n]
# #     else:
# #         e[n] = n*fact(n-1)
# #         return e[n]

# # print(fact(5))
# # print(e)
# #######################################
# #Generators 
# # def h():
# #     x = 0
# #     while True:
# #         yield x
# #         x = x + 2
# # #starts generator
# # x1 = h()

# # print(next(x1))
# # print(next(x1))
# # print(next(x1))
# # print(next(x1))

# # def h():
# #     x = 0 
# #     while True:
# #         yield x
# #         x = x + 2
# # def g(xstop):
# #     for i in h():
# #         if i > xstop:
# #             return i
# #         else:
# #             yield i
# # for i in g(10):
# #     print(i)

# ###################################

# #                               Lecture 17 


# ###################################

# #                               Lecture 18 

# # def f(n):
# #     if n == 0:
# #         return 100
# #     else:
# #         return n - 10 + f(n-1)

# # for i in range(0,6):
# #     print("f({0}) = {1}".format(i,f(i)))

# # Bottom-up memoization ^^ and dictionary outside
# # d = {0:100}

# # def g(n):
# #     if n in d.keys():
# #         return d[n]
# #     else:
# #         for i in range(1,n+1):
# #             d[i] = i - 10 + d[i-1]
# #         return d[n]
# # for i in range(0,6):
# #     print("g{0}) = {1}".format(i,g(i)))

# ####################################################
# #Convergence (Tau)
# # def b(n,alpha,tau):
# #     def bp(n):
# #         if n < tau:
# #             return 0 
# #         else:
# #             return 1 + bp(alpha*n)
# #     return bp(n)

# # tennis_ball = .53
# # super_ball = .85
# # tau = .1
# # print(b(1,tennis_ball,tau))
# # print(b(1,super_ball,tau))

# ####################################################
# #                                           Lecture 19 
# ### List Comprehension 
# # x = [(want) (from) (condition)]

# ### Filter
# # A way to choice things that are true 

# ### Zip
# # Helps with iteration 
# # ^ zip(*z) = unzips 

# ### OOD Class 
# # class Pet:
# #     def __init__(self, pname, tag):
# #         self.name = pname #self is the memory location 
# #         self.tag_id = tag
# #     def get_name(self):
# #         return self.name
# #     def get_tag_id(self):
# #         return self.tag_id
# #     def set_tag_id(self, new_tag):
# #         self.tag_id = new_id
    
# #     def __eq__(self,xpet):
# #         return self.tag_id == xpet.get_tag_id() #Checking rather the tag is the same

# # x = Pet("Ursala", "A12B")
# # y = Pet("Kaiser", "A12B")

# # if y == x:
# #     print("They are the same.")
# # else:
# #     print("Different Dogs.")

# ############################################
# ### Another example 
# # from datetime import date

# # class Person:
# #     programmer = True

# #     def __init__(self,x,d):
# #         self.name = x
# #         self.bd = date(d[2],d[0],d[1])
        
# #     def get_name(self):
# #         return self.name
    
# #     def get_birthdate(self):
# #         return self.bd
    
# #     def get_age(self):
# #         today = date.today()
# #         return today.year - self.bd.year

# # p1 = Person("Bach",(3,31,1685))
# # p2 = Person("Ada",(12,10,1815))

# # print(p2.get_birthdate())
# # print(p2.get_age())

# ########################################################
# #                       Lecture 20 
# # class PiggyBank: 
# #     def __init__(self): #only called once 
# #         #make instance variable called pennies 
# #         self.pennies = 0 

# #     def get_amount(self):
# #         #return total amount of pennies
# #         return round(self.pennies,2)
    
# #     def deposit(self, penny):
# #         self.pennies += .01 

# #     def rainy_day(self,amount):
# #         if amount > self.pennies:
# #             return -1 
# #         else:
# #             self.pennies -= amount 
# #             return amount 


# # # Created two instances eeyore and kitty 

# # eeyore, kitty = PiggyBank(), PiggyBank()

# # ec = [0.01 for i in range(30)]
# # kc = [0.01 for i in range(40)]

# # for i in ec:
# #     eeyore.deposit(i)
# # for i in kc:
# #     kitty.deposit(i)

# # print("eeyore =", eeyore.get_amount())
# # print("kitty =", kitty.get_amount())

# #######################################################



# #######################################################
# #                   Lecture 21

# ######################################################
# #                   Lecture 22 
# # import matplotlib.pyplot as plt 
# # import numpy as np

# # abscissa = np.arrange(20)
# # plt.gca().set_prop_cycle('color', ['red','green','blue','yellow'])

# # # print(abscissa)
# from math import sqrt


# class Vector2d:
#     def __init__(self, x, y=None):
#         #if isinstance(x, Vector2d):
#         if y == None:
#             print('aa')
#             self.x = x.x
#             self.y = x.y
#         else:
#             print('bb')
#             self.x = x
#             self.y = y

#     def __add__(self, other):
#         return Vector2d(self.x + other.x, self.y + other.y)

#     def __repr__(self):
#         return 'x=' + str(self.x) + ', y=' + str(self.y)

#     def __lenght(self):
#         return sqrt(self.x ** 2 + self.y ** 2)

#     lenght = property(fget=__lenght)


# v1 = Vector2d(1, 1)
# v2 = Vector2d(2, 2)
# v3 = v1 + v2

# print(v1.lenght)
# print(v2.lenght)
# print(v3.lenght)
# print(v1 + v2)

# v4 = Vector2d(v3)

#           Lecture 23 
# # Fionacci Sequence # # 
# n = 10 
# a = [0,1]
# for i in range(2,n):
#     a.append(a[i-1]+a[i-2])
# print(a)

# Sorting using Class List 
# x = [5,2,13,4]
# print(x)
# x.sort()
# print(x)

# y = ["cat", "dog", "ant", "gnat"]
# print(y)
# y.sort(reverse=True)
# print(y)

