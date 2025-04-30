def do_smth(msg:str, a, b, c):
    s = f"do_smth with {msg} {a}, {b}, {c}"
    print(s)
  
def do_with_dico(dico):
    for key in dico:
        print(f"{key} --> {dico[key]}")
            
def print(**kwargs):
    print("print_dico")
    for key in kwargs:
        print(f"{key} --> {kwargs[key]}")
  
def test():
    a = 1
    b = 2
    c = 3
    do_smth("3 numbers", a, b, c)

    data = (1, 2, 3)
    do_smth("tuple", *data)
    #do_smth("tuple", data) # this will not work, data is a tuple

    a, b, *rest = range(5)
    print ("range : ", a, b, rest)

    dico = {"a":1, "b":2, "c":3}               
    do_with_dico(dico)
    
    do_smth("dico (keys)", *dico)      # this will display the keys of the dico
    do_smth("dico (values)", **dico)     # this will display the values of the dico
    
    
if __name__ == "__main__":
    try:
        test()
    except Exception as e:
        print(f"Error: {e}")