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