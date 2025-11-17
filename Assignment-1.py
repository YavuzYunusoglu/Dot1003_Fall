state = True
number_count = 0
sum = 0
odd = 0
even = 0

while state:
    num = int(input("dumb calculator v0.1 If you want to exit, enter 0: "))
    if num != 0:
        number_count = number_count + 1
        sum = sum + num
        if(num % 2 == 0):
            even = even + 1
        else:
            odd = odd + 1
    else:
        state = False
print(f"Total number: {number_count}")
print(f"sum: {sum}")
print(f"Mean: {sum / number_count}")
print(f"odd: {odd}, even: {even}")