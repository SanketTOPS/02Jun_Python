data = ["python", "java", "php", "c++", "js"]
# print(data)

"""print(data[0])
print(data[-1])
print(data[0:3])
print(data[2:])
print(data[:3])"""

# ---------------------- #
# print(data)
# print(len(data))
# data[1] = "iOS"  # value update
# print(data)

"""for i in data:
    print(i)"""

# print(data.index("python"))

# print(data)

"""if "PHP" in data:
    print("Yes...")
else:
    print("Noo")"""


# ------------------------------ #
# List Methods
# print(data)
# data.append("html")
# data.insert(2, "css")
# data.remove("c++")
# data.pop()
# data.pop(1)
# data.clear()
# data.sort()
# data.reverse()
# del data[0]
# print(data)


# ------------------------------ #
print(data)

# newdata = data.copy()
# print(newdata)

newdata = ["html", "css", "html5"]
print(newdata)

# print(data + newdata)
data.extend(newdata)
print(data)
