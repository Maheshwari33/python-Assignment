#input from user
n= int(input("how many numbers:"))
lst=[]
for n in range (n):
   numbers= int(input("enter a number:"))
   lst.append(numbers)
   print("sum of the numbers is:",sum(lst))


#smallest_largest
ls=[]
for i in range(5):
   num=int(input("enter the first number:"))
   num=int(input("enter the second number:"))
   ls.append(num)
   ls.sort()
   print("smallest number is:",ls[-0])
   print("largest number is:",ls[-1])


#ascending_descending

#ascending
ls=[67,2,999,1,15]
print("unordered list:",ls)
ls.sort()
print("ordered list:",ls)


#descending
names=["mahii","aasha","ridhi","nisha"]
print("unsorted:",names)
names.sort(reverse=True)
print("sorted:",names)


#list in tuple
t=(1,2,3,4,5,6)
ls=list(t)
print(ls)
print(type(1))


#deleted list
ls=[1,2,3,4,5,6,7,8,9,10]
del ls[5]
print(ls)