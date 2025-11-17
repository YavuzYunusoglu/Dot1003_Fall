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

