# step1_conversion.py

# int(): 从数字或字符串返回一个整数对象。
num_str = "123"
num_int = int(num_str)
print(f"String '{num_str}' as integer: {num_int}")

# str(): 返回对象的字符串版本。
int_val = 456
str_val = str(int_val)
print(f"Integer {int_val} as string: '{str_val}'")

# list(): 从可迭代对象（iterable）创建一个新的列表。
my_tuple = ("a", "b", "c")
my_list = list(my_tuple)
print(f"Tuple {my_tuple} as list: {my_list}")

# dict(): 创建一个新的字典。
my_pairs = [("x", 1), ("y", 2)]
my_dict = dict(my_pairs)
print(f"List of pairs {my_pairs} as dict: {my_dict}")

# type(): 返回一个对象的类型。
print(f"Type of num_int: {type(num_int)}")

# isinstance(): 如果对象是某个类的实例，则返回 True。
is_list = isinstance(my_list, list)
print(f"Is my_list an instance of list? {is_list}")
