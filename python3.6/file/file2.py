#!/usr/bin/python3

# 打开一个文件
f = open("./tmp/foo.txt", "r")

# content = f.read()
# content = f.readline()
# content = f.readlines()

for line in f:
    print(line, end='')

# print(content)

# 关闭打开的文件
f.close()