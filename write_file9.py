

# #it will creat new file and writ a below twxt in it
# str="heyy saad how ar u ,is everythin okkky"
# f=open("myfile.txt","w")
# f.write(str)
# f.close()


 #it can print list of all lines in file and print it
# f=open("file.txt")
# lines=f.readlines()
# print(lines,type(lines))
# f.close()

#   #this will read only line 2
# f=open("file.txt")
# line2=f.readlins()
# print(line2,type(line2))
# f.close()

#   #it will print all line 
# f=open("file.txt")
# line= f.readline()
# while(line!=""):
#     print(line)
#     line=f.readline()
# f.close()

#  #append it will add text in last
# str="heyy saad how ar u ,is everythin okkky"
# f=open("myfile.txt","a")
# f.write(str)
# f.close()

 #with statement wich no need to close file it can close atomaticaly
with open("file.txt")as f:
    print(f.read())
      