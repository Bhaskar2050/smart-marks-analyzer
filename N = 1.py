# with open(r"D:\Python\practice.txt", 'w') as f:
#     f.write("Hi everyone \nwe are learning File I/O \nusing Java \nI like programing in Java ")

# with open(r"D:\Python\practice.txt") as f:
#     content = f.read()

# new_content = content.replace("Java", "Python")

# with open(r"D:\Python\practice.txt", 'w') as f:
#     f.write(new_content)


# with open(r"D:\Python\practice.txt", 'r') as f:
#     content = f.read()
#     if "learning" in content:
#         index = content.index("learning")
#         print("'learning' found at index: " , index)

with open(r"D:\Python\practice.txt", 'r') as f:
    content = f.read()

if "learning" in content:
    index = content.index("learning")
    print("'learning' found at index: ", index)