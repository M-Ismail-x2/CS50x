# get height input (int betweeen 1-8)
while (True):
    try:
        height = int(input("Height: "))
    except ValueError:
        continue
    else:
        if height >= 1 and height <= 8:
            break
        else:
            continue

# print the wall
for i in range(1, height + 1):
    print(" " * (height - i), end="")
    print("#" * i, end="")
    print("  ", end="")
    print("#" * i)
