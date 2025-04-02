def get_positional_args(**kwargs):
    print(kwargs)
    
#get_positional_args("Hello", "World", "Python") # This will raise an error because the function expects keyword arguments, not positional arguments.#
get_positional_args(hello="Hello", world="World", python="Python") # This will work because we are passing keyword arguments.

def get_all_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    
get_all_args()
get_all_args("Hello", "World")
get_all_args(c=2, d=3, e=4)
get_all_args(3, 4, h="ttt", d=3)