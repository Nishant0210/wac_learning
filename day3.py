
# list
# list=[1,2,'nishant', True ]
# print(list)
# print(type(list))

# use of .split()

# l='1 2 3 4'
# n=l.split()
# print(n)

# l='hi-this-is-nishant'
# n=l.split('-')
# print(n)

# whenever we want to use .split() function pass the argument ... default argument is space

# list=[1 , 10 , 'nishant' , ['hello' , 'bye']]
# print(list)

# modify list
# list[1]='ulhare'
# print(list)

#delete element
# del(list[1])
# print(list)

#append elemet or list / add element at end
# list=[1 , 10 , 'nishant' , ['hello' , 'bye']]
# print(list)
# list.append('ulhare')
# print(list)

# negative indexing
# list=[1 , 10 , 'nishant' , ['hello' , 'bye']] #last index is -1 
# print(list[-1])

# list slicing

# list=[1 , 10 , 'nishant' , ['hello' , 'bye']] 
# print(list[:-1])   # last element is excluded 0:3 means 3 is excluded
# print(list[::-1])  //reverse list



#list formnation
# list=[]
# n=int(input())
# for i in range(n):
#     k=input()
#     list.append(k)

# print(list)


#-------------------------------- functions -----------------------

# def is_even(n):
#     if(n%2==0):
#         return True
#     else:
#         return False

# m=int(input())
# print(is_even(m))

#multiple returns

# def c(a,b):
#     return(a+b,a-b,a*b)

# sum, sub, mul=c(5,4)
# print(sum,sub,mul)

a=[1 , 2, 3, 4, 5]
print(a[3:0:-1])