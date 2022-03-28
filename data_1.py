data = [23, 56, 34, 78, 80, 40,
            32, 62, 19, 90, 77, 100, 47, 61, 73, 84, 98, 5, 10, 30]
d = sorted(data)
print("List has been Ordered {} (Low to High)".format(d))

min_value = 20
max_value = 80

for index in range(len(data) - 1, - 1, - 1):
        if data[index] < min_value or data[index] > max_value:
            print(index, data)
            del data[index]
print(data)

data.sort()
print("Final Sorted Version After Eliminating Outliers: {0}\nWhere Range Value contains Minimum Value {1} and Maximum Value {2}".format(data, min_value, max_value))

#Second Step:

data_age = [13, 20, 24, 12, 11, 30, 25, 40, 48, 15, 33]

top_index = len(data_age) - 1

min_age = 20
max_age = 40

for index, value in enumerate(reversed(data_age)):
    if value < min_age or value > max_age:
        print(top_index - index, value)
        del data_age[top_index - index]

print(data_age)