import os

dirs = os.listdir()

count = 0
for i in dirs:
    print(i)
    count += 1

print("Total:", count)