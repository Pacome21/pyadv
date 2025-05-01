class ImVeryLong:
    def __len__(self):
        return 12000
    
a = ImVeryLong()
print(len(a))  # 12000

class MyFile:
    def __init__(self):
        self.data = ""
    def read(self, size):
        return self.data[:size]
    def write(self, data):
        self.data += data
    def close(self):
        pass        

f = MyFile()
f.write("Hello")
print(f.read(5))  # Hello
print(" world", file=f)
print(f.read(100))  #  world

class Hello:
    def __init__(self, name, age=0):
        self.age = age
        self.name = name

    def __enter__(self):
        print(f"Hello {self.name}")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Goodbye {self.name}")
    def __str__(self):
        return f"I am {self.name} and I am {self.age} years old"

def testCms():
    with Hello("Christophe", 56) as hello:
        print(hello)
        hello.age = 10
        hello.age = 10
        print(hello)

testCms()