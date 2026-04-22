# step5_introspection.py


class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alice", 30)

# hasattr(): 如果对象具有指定的属性，则返回 True。
print(f"Does person have 'name' attribute? {hasattr(p, 'name')}")
print(f"Does person have 'height' attribute? {hasattr(p, 'height')}")

# setattr(): 它是 getattr() 的对应函数。它设置对象上的一个属性。
print("Setting attribute 'height' to 175...")
setattr(p, "height", 175)
print(f"Does person have 'height' attribute now? {hasattr(p, 'height')}")

# getattr(): 返回对象指定属性的值。
print(f"Person's name: {getattr(p, 'name')}")
print(f"Person's height: {getattr(p, 'height')}")

# dir(): 返回当前局部作用域或对象属性中的名称列表。
# 我们检查 'height' 是否现在在属性列表中。
print(f"Is 'height' in dir(p)? {'height' in dir(p)}")

# globals(): 返回当前全局符号表（symbol table）的字典。
# 我们将检查我们的 'Person' 类是否在 globals 中。
print(f"Is 'Person' in globals? {'Person' in globals().keys()}")


# locals(): 返回当前局部符号表的字典。
def a_func():
    x = 10
    print(f"Is 'x' in locals()? {'x' in locals().keys()}")


a_func()
