#Task 40

city_name = input("Wich city: ")
repetition = int(input("How many repetition for 'li': "))
print(f"{city_name}{"li" * repetition}lerle")


#Task 41

usr_inp1 = input("First word: ")
usr_inp2 = input("Second word: ")
if(len(usr_inp1) > len(usr_inp2)):
    print(usr_inp1)
elif(len(usr_inp1) < len(usr_inp2)):
    print(usr_inp2)
else:
    print("Their length are same")


print("")#Task42

usr_inp3 = input("Your input: ")
print(f"*{usr_inp3}*")


print()#Task43

usr_inp4 = input("Your input: ")
print(usr_inp4)
print("-" * len(usr_inp4))


print("")#Task44

u_input = input("Your input: ")
if(len(u_input) > 18):
    print("Please enter an input less than 18.")
print("-" * 20)
if(len(u_input) % 2 == 0):
    print(f"|{">" * int(((18 - len(u_input)) / 2))}{u_input}{"<" * int((18 - len(u_input)) / 2)}|")
else:
    print(f"|{">" * int(((18 - len(u_input)) / 2))}{u_input}{"<" * int((18 - len(u_input)) / 2)}<|")
print("-" * 20)


print("")#Task45

usr_inp5 = input("Please enter string: ")
first_int = int(input("Please enter first integer: "))
second_int = int(input("Please enter second integer: "))
print(usr_inp5[first_int:second_int])


print("")#Task46

usr_inp6 = input("Please enter string: ")
usr_int = int(input("Please enter an integer: "))
print(usr_inp6[usr_int:])


print("")#Task47

usr_inp7 = input("Please enter string: ")
usr_int1 = int(input("Please enter an integer: "))
print(usr_inp7[:1])


print("")#Task48

usr_inp8 = input("Please enter string: ")
if("a" in usr_inp8):
    print("Found")
else:
    print("Not found")


print("")#Task49

usr_inp9 = input("Please enter string: ")
srch_item = input("Please enter search item: ")
if(srch_item in usr_inp9):
    print("Found")
else:
    print("Not found")


print("")#Task50
usr_inp10 = input("Please enter string: ")
srch_item = input("Please enter search item: ")
if(srch_item in usr_inp10):
    print(f"Found it at {usr_inp10.find(srch_item)}")
else:
    print("Not found")


print("")#Task51

text = "The quick brown fox jumps over the lazy dog"
state = True
while state:
    inp = input("Where are you looking for: ")
    if(inp == "-1"):
        print("Bye.")
        state = False
    else:
        if(inp in text):
            print(f"Found it at {text.find(inp)}")

        else:
            print("Not Found")

_list = [1.2345, 2.3456, 3.4567, 4.5678]
newlist = []
def to_two_decimal(orginal_list):
    for i in orginal_list:
        newlist.append(float("{:.2f}".format(i)))
to_two_decimal(_list)
print(newlist)

input("")