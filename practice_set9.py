#  #Q1
# f=open("poem.txt")
# content=f.read()
# if("twinkle"in content):
#     print("The twinkle is preaent in this")
# else:
#     print("NOT prestnt in thid")
# f.close()

#   #Q2
# import random
# def game():
#     print("you are playing the game:")
#     score=random.randint(1,62)
    
#     with open("hiscore.txt") as f:
#         hiscore=f.read()
#         if(hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0
#     print(f"your hiscoer:{score}")
#     if(score>hiscore):
        
#         with open("hiscore.txt","w")as f:
#             f.write(str(score))

#     return score
# game()
    
  #Q3
# import os

# # Create the folder if it doesn't exist
# os.makedirs("tables9_prac", exist_ok=True)

# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} x {i} = {n * i}\n"
    
#     with open(f"tables9_prac/table_{n}.txt", "w") as f:
#         f.write(table)

# # Generate multiplication tables from 2 to 20
# for i in range(2, 21):
#     generateTable(i)

   #Q4

# word ="donkey"

# with open("file9.txt" ,"r") as f:
#     content =f.read()

# contentNew= content.replace(word,"#####")

# with open("file9.txt" ,"w") as f:
#    f.write(contentNew)

  #Q5
# words=["saad","yash","ADCET"]
# with open("file9.txt" ,"r") as f:
#     content =f.read()
# for word in words:
#  content= content.replace(word,"*"*len(word))

# with open("file9.txt" ,"w") as f:
#    f.write(content)

  #Q6


# with open("log9.txt","r")as f:
#    content= f.read()
# if "python "in content:
#    print("yes")
# else:
#    print("NO it is not")
# f.close()

  #Q7

# with open("log9.txt")as f:
#  lines= f.readlines()

# lineno=1
# for line in lines:
#    if ("python" in line):
#     print(f"yes python is present line no:{lineno}")
#     break
#    lineno+=1
# else:
#    print("NO it is not")

#   #Q8
# with open("file9.txt") as f:
#     content =f.read
# with open("this_copy9.txt","w") as f:
#     f.write(content)

 #Q9
# with open("file9.txt") as f:
#     content1 =f.read()
# with open("log9.txt")as f:
#     content2=f.read()
# if (content1==content2):
#     print("yes it is has same content ")
# else:
#     print("NO it is has no same content ")
#     #this both file has no same content

#  #Q10
# with open("wipe9.txt","w") as f:
#     f.write("")# it will wipe/clear all content in this file

  #Q11
with open("old9.txt") as f:
    content=f.read()
with open("rename9.txt","w") as f:
    f.write(content)
    # it will creat new file and past as same as old.txt