  #dictnary
d={} #it is an empty dictnary
marks={
    "saad":90,
    "xyz":50,
    "wxy":34
}
print(marks,type(marks))

 #dict methods
# print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"saad":99,"dfsf":98})
print(marks.get("saad"))