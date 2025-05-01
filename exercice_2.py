class CodeDelimiter:
    def __init__(self, delimiter, length=50):
        self.delimiter = delimiter
        self.length = length

    def __enter__(self):
        print(self.delimiter * self.length)
        print(f"Delimiter: {self.delimiter}, Length: {self.length}")

    def __exit__(self, exc_type, exc_value, traceback):
        print(self.delimiter * self.length)

with CodeDelimiter("=", 50):
    print("This is a test of the CodeDelimiter class.")
