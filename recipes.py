with open('recipes.txt') as f:
  cookbook = dict
  data = f.read()
  print(type(data))
  print(data)

# data += '\nЕще одна строка'
# print(data)

# with open('test.txt') as f:
#   print(f.readline().strip())
#   print(f.readline().strip())
#   print(f.readline().strip())
#   print(f.readline().strip())
#   print(f.readline().strip())
#   print(f.readline() == '')
#   print(f.readline() is None)
#   # print(f.readline() is None)

# with open('test.txt') as f:
#   lines = f.readlines()
#   print(type(lines))
#   print(len(lines))
#   print(lines[1])

# with open('test.txt') as f:
#     for l in f:
#         print(l.strip())
#
#
# with open('test.txt') as f:
#     for idx, l in enumerate(f):
#         print(idx, l.strip())