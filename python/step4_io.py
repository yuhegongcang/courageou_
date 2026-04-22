# step4_io.py
import datetime

# open(): 打开一个文件并返回一个相应的文件对象。
# 我们使用 'with' 语句来确保文件被自动关闭。
file_path = "/home/labex/project/my_file.txt"
with open(file_path, "w") as f:
    f.write("Hello, LabEx!\n")
    f.write("This is a test file.")
print(f"Successfully wrote to {file_path}")

# 从文件中读取
with open(file_path, "r") as f:
    content = f.read()
    print("--- File Content ---")
    print(content)
    print("--------------------")

# repr(): 返回一个包含对象的可打印的、无歧义的表示的字符串。
now = datetime.datetime(2023, 10, 27, 10, 30, 0)
print(f"str(now): {str(now)}")
print(f"repr(now): {repr(now)}")

# format(): 将一个值转换为“格式化”的表示。
formatted_string = format(123.4567, ".2f")
print(f"Formatted number (123.4567 to .2f): {formatted_string}")
