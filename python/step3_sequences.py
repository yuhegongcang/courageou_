# step3_sequences.py

my_list = [3, 1, 4, 1, 5, 9]
print(f"Original list: {my_list}")

# len(): 返回对象的长度（项的数量）。
print(f"Length of the list: {len(my_list)}")

# sorted(): 从可迭代对象的项中返回一个新的已排序列表。
print(f"Sorted list: {sorted(my_list)}")

# reversed(): 返回一个反向迭代器。我们将其转换为列表以便打印。
print(f"Reversed list: {list(reversed(my_list))}")

# enumerate(): 返回一个枚举对象（索引、值对的迭代器）。
print(f"Enumerated list: {list(enumerate(my_list))}")

# map(): 返回一个迭代器，它将一个函数应用于可迭代对象的每个项。
squared_numbers = map(lambda x: x * x, my_list)
print(f"Squared numbers (map): {list(squared_numbers)}")

# filter(): 从可迭代对象中构造一个迭代器，该迭代器的函数返回 true。
even_numbers = filter(lambda x: x % 2 == 0, my_list)
print(f"Even numbers (filter): {list(even_numbers)}")

# zip(): 并行迭代多个可迭代对象。
list_a = ["a", "b", "c"]
list_b = [1, 2, 3]
zipped = zip(list_a, list_b)
print(f"Zipped lists: {list(zipped)}")
