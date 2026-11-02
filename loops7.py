  #loops
  # for loop
for i in range(1,101,2): #2 is step size
    print(i)

 #while loops

i=1 
while(i<51):
    print(i)
    i+=1 # or i=i+1

# while
l=["saad","momin",11,"rohan","shubhem"]
i=0
while(i<len(l)):
    print(l[i])
    i+=1

   #for
for i in range (4,): 
    print(i)

#for loop in list
l =[2,4,57,64,6634,74,6456,534]
for i in l:
    print(i)

# for loop in tuple
t=(34,45,745,674,56,46,)
for i in t:
    print(i)

# for loops with strings
s="saad"
for i in s:
    print(i)
 
# for loops with else
l=[2,5,6,76]
for i in l:
    print(i)
else:
    print("done") # this will print when loop exhaust

 #break
for i in range(100):
    if(i==34):
        break #exit the loop
    print(i)
 #continue
for i in range(100):
    if(i==34):
       continue #skip this iteration
    print(i)
 #paas
if i in range(200):
    pass #without pass program will thow error
i=0
while(i<=26):
    print(i)
    i+=1


