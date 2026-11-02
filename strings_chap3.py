a= 'saad'
b="saad"
c='''saad'''
legth=len(a)#print length of the string
print(legth)
a=(a[0:3])
print(a)
print(a[-3:-1])
print(a[0:3])
print(a[:3])
name="saad momin"
print(name[0:7:2])

print(name.endswith("min"))
print(name.startswith("saa"))
print(name.capitalize())





#🔥 1️⃣ lower()
# Convert a string to lowercase.

# s = "Hello World"
# print(s.lower())  # Output: "hello world"

# 🔥 2️⃣ upper()

# Convert a string to uppercase.

# s = "hello world"
# print(s.upper())  # Output: "HELLO WORLD"

# 🔥 3️⃣ capitalize()

# Capitalize the first character of the string.

# s = "hello world"
# print(s.capitalize())  # Output: "Hello world"

# 🔥 4️⃣ title()

# Capitalize the first character of every word.

# s = "hello world"
# print(s.title())  # Output: "Hello World"

# 🔥 5️⃣ strip() / lstrip() / rstrip()

# Remove whitespace from both ends (or left/right) of the string.

# s = "  hello world  "
# print(s.strip())   # Output: "hello world"
# print(s.lstrip())  # Output: "hello world  "
# print(s.rstrip())  # Output: "  hello world"

# 🔥 6️⃣ replace()

# Replace a substring with another.

# s = "hello world"
# print(s.replace("hello", "hi"))  # Output: "hi world"

# 🔥 7️⃣ split()

# Split a string into a list based on a separator.

# s = "hello world"
# print(s.split())  # Output: ["hello", "world"]

# 🔥 8️⃣ join()

# Join a list of strings with a separator.

# words = ["hello", "world"]
# print(" ".join(words))  # Output: "hello world"

# 🔥 9️⃣ find() / index()

# Find the position of a substring.

# s = "hello world"
# print(s.find("world"))  # Output: 6
# # index() is similar but raises an error if not found

# 🔥 🔟 startswith() / endswith()

# Check if a string starts or ends with a specific substring.

# s = "hello world"
# print(s.startswith("hello"))  # True
# print(s.endswith("world"))    # True

# 🔥 1️⃣1️⃣ count()

# Count occurrences of a substring.

# s = "hello world hello"
# print(s.count("hello"))  # Output: 2

# 🔥 1️⃣2️⃣ isalpha() / isdigit() / isalnum()

# Check the nature of the string.

# "hello".isalpha()  # True
# "123".isdigit()    # True
# "hello123".isalnum() # True