#Task21
def Print_Argument(name):
    print("Hello", name)
Print_Argument(input("Please input an argument: "))


print("")#Task22

def Print_Name(name2):
    return name2
print(f"Hello {Print_Name(input("Please input a name."))}")


print("")#Task23
def sum(arg1, arg2):
    return (arg1+arg2)
print(sum(2, 3))


print("")#Task24

def greeting(input_name):
    print(f"Hi {input_name}")
greeting("Andrew Ryan")
greeting("Gordon Freeman")


print("")#Task25

def mean(arg1, arg2, arg3):
    return (arg1+arg2+arg3) / 3
print(mean(3,2,1))


print("")#Task26

state = True
while state:
    usr_inp = input("Say my name: ")
    if(str.lower(usr_inp) == "heisenberg"):
        print("You're goddamn right.")
        state = False


print("")#Task27
state2= True
password = input("Enter you password: ")
while state2:
    password_again = input("Enter again: ")
    if password_again == password:
        print("Your password matches and account created successfully")
        state2 = False
    else:
        print("They are not same.")


print("")#Task28

state3 = True
usr_inpt2 = int(input("Please enter a number: "))
while state3:
    if(usr_inpt2 == 0):
        state3 = False
        print("Kaboom")
    else:
        usr_inpt2 = usr_inpt2 - 1


print("")#Task29
state4 = True
true_password = 123123
count = 3
while state4:
    password_try = input("Password: ")
    if(password_try == true_password):
        state4 = False
        print("Welcome.")
    else:
        if(count == 0):
            state4 = False
            print("Incorrect Password. Exterminate...")
        else:
            print("Try again.")


print("")#Task30
#assignment-1 from repo


#Task31

mylist = ["My first item", "my second item", "my last item"]
print(mylist[0])
print(f"List length is {len(mylist)}")
mylist.remove(2)
print(mylist)

#Task 32

mylist2 = ['my first item', 'my second item', 'my last item']
print(mylist2)
mylist2[1] = "My new item"
print(mylist2)

#Task33
mylist3 = []
state5 = True
while state:
    usr_inp3 = input("Please enter an input(enter 'exit' for exit): ")
    if(str.lower(usr_inp3) == "exit"):
        state = False
    else:
        mylist3.append(usr_inp3)
print(mylist3)


print("")#Task34

for i in mylist3:
    print(i)

usr_inp4 = input("Please enter an input: ")
for i in usr_inp4:
    print(i)

print("")#Task35

mylist4 = [1, 2 ,1 ,3]
total_point = 0
for i in mylist4:
    total_point = total_point + i
print(f"Total {total_point} points earned.")


print("")#Task36
mylist5 = [1, -2, 1, 3, -5, 7, 0]
total_point2 = 0
for i in mylist5:
    if(i > 0):
        total_point2 = total_point2 + i
print(f"Total {total_point2} points earned")


print("")#Task37
box_size = int(input("Please input table size: "))
count2 = box_size
state6 = True
while state6:
    if(count2 == 0):
        state6 = False
    else:
        print(f"{"|_" * box_size}|")
        count2 = count2 -1 