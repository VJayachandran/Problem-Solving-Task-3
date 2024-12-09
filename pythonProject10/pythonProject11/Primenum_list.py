#Creating a list of numbers
mylist=[10, 501, 22, 37, 100, 999, 87, 351]
prime=[]
#check the defined list in conditions
for i in mylist:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
#append method adds an item to the end of the list
        prime.append(i)
#print the output
        print("Prime number in the given list:",prime)