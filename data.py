data = [30, 45, 25, 80, 125, 136, 74, 52, 66, 90, 101, 155, 233, 312, 520]
j = sorted(data)
print(j)
del j[0:2]
print(j)
del j[0:7]
print(j)

min_valid = 100
max_valid = 200

for index, value in enumerate(j):
    if (value < min_valid) or (value > max_valid):
        del j[index]
        index -= 1       #another example
print(j)


#Including Only Min and Max Value
stop = 0
j_1 = sorted(data)
for index, value in enumerate(j_1):
    if value >= min_valid:
        stop = index
        break

print(stop)
del j_1[:stop]
print(j_1)

start = 0
j_2 = sorted(data)

for index in range (len(j_2) - 1, -1, -1):
    if j_2[index] <= max_valid:
        start  = index + 1
        break

print(start)
print(j_2)
del j_2[start:]
print(j_2)

data_1 = [1109, 1689, 1342, 1455, 1112,
          1322, 1790, 1900, 1592, 1290]
min_valid_1 = 1200
max_valid_1 = 1800

stop = 0
for index, value in enumerate(data_1):
    if value >= min_valid_1:
        stop = index
        break
print(data_1)
