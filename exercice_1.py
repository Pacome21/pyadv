"""
This module demonstrates the use of function arguments in Python.
"""
def get_positional_args(**kwargs):
    """
    This function accepts keyword arguments and prints them.
    """
    print(get_positional_args.__name__)
    print(get_positional_args.__doc__)
    print("Positional arguments:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# This will raise an error because the function expects keyword arguments, not positional arguments.
#get_positional_args("Hello", "World", "Python")

# This will work because we are passing keyword arguments.
get_positional_args(hello="Hello", world="World", python="Python")


def get_all_args(*args, **kwargs):
    """
    This function accepts both positional and keyword arguments and prints them.
    """
    print(get_all_args.__name__)
    print(get_all_args.__doc__)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

get_all_args()
get_all_args("Hello", "World")
get_all_args(c=2, d=3, e=4)
get_all_args(3, 4, h="ttt", d=3)
