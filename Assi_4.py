#loop mainipulation 
a="string"
for i in a:
    print(i)

a="string"
for i in 1,2,3,4,5:
   print(i)


#or...with else loop using break
a="string"
for i in a:
    if i=="i":
      break
    else:
      print(i)
else:
      print("this has break")

 #for...with else loop using pass
a="string"
for i in a:
    if i=="i":
         pass
    else:
       print(i)
else:
      print("this has pass")    

#for...with else loop using continue
a="string"
for i in a:
    if i=="i":
        continue
    else:
        print(i)
else:
    print("this has continue")    



#while...with else loop using break
i=1
while i<=10:
    if i==5:
       break
    else:
       print(i)
    i+=1
else:
   print("this has break")

#while... with else loop  using pass
i=1
while i<=10:
    if i==5:
        pass
    else:
        print(i)
    i+=1
else:
   print("this has pass")


#while... with else loop using continue  
i=1
while i<=10:
    if i==5:
        continue
    else:
        print(i)
    i+=1
else:
    print("this has continue")    