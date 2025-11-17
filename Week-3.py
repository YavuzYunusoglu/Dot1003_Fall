#Task21
def Print_Argument(name):
    print("Hello", name)
Print_Argument(input("Please input an argument: "))


print("")#Task22

def Print_Name(name2):
    return name2
print(f"Hello {Print_Name(input("Please input a name."))}")


print()#Task23
def sum(arg1, arg2):
    return (arg1+arg2)
print(sum(2, 3))


print("")#Task24

def greeting(input_name):
    print(f"Hi {input_name}")
greeting("Andrew Ryan")
greeting("Gordon Freeman")


print()#Task25

def mean(arg1, arg2, arg3):
    return (arg1+arg2+arg3) / 3
print(mean(3,2,1))
