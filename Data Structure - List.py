L= [11,12,13,14]
print("THE LIST IS ",L)
L.append(50) #adding 50
L.append(60) #adding 60
del L[0] #deleting 11
del L[1] #deleting 13
L.sort() #ascending order
L.sort(reverse=True) #descending order
print("THE LIST NOW IS :",L)
print("IS 13 IN THE LIST - ",13 in L) # searching 13
print("NUMBER OF ELEMENTS ",len(L)) #counting the number of elements
print("The sum of elements is :",sum(L)) #sum of all the elements in the list
s =0 #Sum of even number
for i in L:
    if i%2 == 0:
        s =s+i
print("Sum of even number is ",s)
r =0 #sum of odd number
for i in L:
    if i%2 != 0:
        r =r+i
print("Sum of odd number is ",r)
p=0 # sum of prime number
for i in L:
    if i%2 != 0 & i%3!=0:
        p =p+i
print("Sum of prime number is ",p)
L.clear() #To clear all elements
del L #To delete L