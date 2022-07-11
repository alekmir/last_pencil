from random import randint


while True:
    try:
        pen_count = int(input("How many pencils would you like to use: "))
    except ValueError:
        print("The number of pencils should be numeric")
    else:
        if pen_count <= 0:
            print("The number of pencils should be positive")
        else:
            break
while True:
    name = input("Who will be the first (John, Jack): ")
    if name not in ["John", "Jack"]:
        print("Choose between *John* and *Jack*")
    else:
        break
while pen_count > 0:
    print(pen_count * '|')
    if name == "John":
        move_count = input(f"{name}'s turn:\n")
    else:
        if pen_count == 1:
            move_count = 1
        elif pen_count % 4 == 1:
            move_count = randint(1, 3)
        else:
            move_count = pen_count - (4 * ((pen_count - 1) // 4) + 1)
        print(f"Jack's turn:\n{move_count}")
    if str(move_count) not in ["1", "2", "3"]:
        print("Possible values: '1', '2' or '3'")
    elif int(move_count) > pen_count:
        print("Too many pencils were taken")
    else:
        pen_count -= int(move_count)
        if pen_count >= 1:
            if name == "John":
                name = "Jack"
            else:
                name = "John"
        elif pen_count == 0:
            if name == "John":
                name = "Jack"
            else:
                name = "John"
print(name, "won!")
