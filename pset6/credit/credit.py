def card_type(num):
    if ((len(num) in [13, 16]) and int(num[0]) == 4):
        return "VISA"
    elif len(num) == 15 and int(num[0:2]) in [34, 37]:
        return "AMEX"
    elif len(num) == 16 and int(num[0:2]) in range(51, 56):
        return "MASTERCARD"
    else:
        return "INVALID"


def sum1(num):
    sum = 0
    for i in num[-2::-2]:
        if int(i) < 5:
            sum += int(i) * 2
        else:
            sum += (int(i) * 2 % 10) + 1
    return sum


# Iterate backwards over input from last number and adding numbers to sum
def sum2(num):
    sum = 0
    for i in num[::-2]:
        sum += int(i)
    return sum


num = input("Number: ")
type = card_type(num)
firstSum = sum1(num)
secondSum = sum2(num)

# if total sum ends with 0
if (firstSum + secondSum) % 10 == 0:
    print(type)
else:
    print("INVALID")
