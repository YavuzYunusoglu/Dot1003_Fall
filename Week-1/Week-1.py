print('Robin will wear their feathery fire,\nWhistling their whims on a low fence-wire;\nAnd not one will know of the war,\nnot one')


print(" ")#Task2

print(f"hours in a week: {24 * 7}")
print(f"Minutes in a week: {60*24*7}")
print(f"Seconds in a week: {24*7*60*60}")


print("")#Task3

print("What is your name?")
name = input("")
print("What is your email adress?")
email= input("")
print("What is your nickname?")
nickname = input("")
print(f"Your name: {name}\nYour email adress: {email}\nYour nicnkanme: {nickname}")
print(F"{name} | {email} | {nickname}")


print("")#Task4

mario = input("Enter a name: ")
princess = input("Enter a victim: ")
print(f"Thank you, {mario}\nBut our {princess} is in another castle!")


print("")#Task5

name4 = "Courier"
age4 = 34
city4 = "New vegas"
print(f"Hi {name4}, you are {age4} years old. You live in {city4}.")


print("")#Task6

name5 = "Ozan Akyol"
age5 = 18
skill1 = "python"
level1 = "beginner"
skill2 = "2d art"
level2 = "beginner"
lower = 2000
upper = 3000
print(f"My name is {name5}i I am 18 years old")
print("")
print("My skills are")
print(f"- {skill1} ({level1})")
print(f"- {skill2} ({level2})")
print("")
print(f"My salary expectation is {lower}-{upper} euros/month")


print("")#Task7

number1 = 3
number2 = 5
print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")
print(f"{number1} / {number2} = {number1 / number2}")


print("")#Task 8

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
if(height > 3):
    BMI = weight / ((height/100) ** 2)
    print(f"Your BMI is {BMI}")
else:
    BMI = weight / (height **2)
    print(f"Your BMI is {BMI}")


print("")#Task 9

game = input("Enter a game name: ")
release_year = int(input("Wich year was this game released: "))
print(f"{game} is {2025-release_year} years old")
num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in the second number: "))
num3 = int(input("Please type in the third number: "))
product = num1 * num2 * num3
print(f"The product is {product}")


print("")#Task10

how_many_times_caffe = 5
lunch_price = 25
groceries_price = 300
average_caffe = how_many_times_caffe * lunch_price / 7
average_groceries = groceries_price / 7
average_daily = average_caffe + average_groceries
print(f"Daily: {average_daily}")
print(f"Weekly: {average_daily * 7}")
print(f"Montly: {average_daily * 30}")
