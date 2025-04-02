def do_smth(a, b, c):
    print(a, b, c)
    
data = (1, 2, 3)

do_smth(*data)

a, b, *rest = range(5)
print (a, b, rest)

def do_with_dico(**kwargs):
    for key in kwargs:
        print(f"{key} --> {kwargs[key]}")
              
do_with_dico(a=1, b=2, c=3, first_name="John", last_name="Doe")