# #it will mearge both dictinary
# dict1={'a':1,'b':2}
# dict2={'b':3,'c':4}
# merge=dict1|dict2
# print(merge)


with (
    open('file.txt') as f1,
    open('old9.txt') as f2
):
    data1 = f1.read()
    data2 = f2.read()

print(data1)
print(data2)