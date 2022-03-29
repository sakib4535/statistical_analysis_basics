import timeit

max_value = 400
min_value = 50
max_valid = 200

value_list1 = list(range(max_value))
value_list2 = list(range(max_value))
value_list3 = list(range(max_value))

def sanitise_1(data):
    stop = 0
    for index, value in enumerate(data):
        if value <= min_value:
            stop = index
            break

    del data[:stop]

    start = 0
    for index in range(len(data) - 1, - 1, - 1):
        if data[index] <= max_valid:
            start = index + 1
            break

    del data[start:]

def sanitise_2(data):
    top_index = len(data) - 1
    for index, value in enumerate(reversed(data)):
        if value < min_value or value > max_value:
            del data[top_index - index]

def sanitise_3(data):
    for index in range(len(data) - 1, - 1, - 1):
        if data[index] < min_value or data[index] > max_valid:
            del data[index]

if __name__ == "__main__":
    print("Timing")
    x = timeit.timeit("sanitise_1(value_list1)",
                       setup="from __main__ import sanitise_1,"
                              "value_list1",
                        number=1)
    print("{:50.61f}".format(x))
    y = timeit.timeit("sanitise_2(value_list2)",
                       setup="from __main__ import sanitise_2,"
                             "value_list2",
                       number=1)
    print("{:50.61f}".format(y))
    z = timeit.timeit("sanitise_3(value_list3)",
                       setup="from __main__ import sanitise_3,"
                             "value_list3",
                       number=1)
    print("{:50.61f}".format(z))

    sanitise_1(value_list1)
    print(value_list1)
    sanitise_2(value_list2)
    print(value_list2)
    sanitise_3(value_list3)
    print(value_list3)