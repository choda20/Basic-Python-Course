def ex321():  # 3.2.1
    print(
        "\"Shuffle, Shuffle, Shuffle\", say it together!\nChange colors and directions,\nDon't back down and stop the "
        "player!\n\t\tDo you want to play Taki?\n\t\tPress y\\n")


def ex333():  # 3.3.3
    encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
    print(encrypted_message[-1::-2])


def ex342():  # 3.4.2
    user_input = input("Enter a string: ")
    print(user_input[0] + user_input[1:].replace(user_input[0], "e"))


def ex343(): # 3.4.3
    user_input = input("Enter a string: ")
    half_length = len(user_input) // 2
    print(user_input[0:half_length].lower() + user_input[half_length:].upper())


if __name__ == '__main__':
    print("ex 3.2.1: ")
    ex321()
    print("\nex 3.3.3: ")
    ex333()
    print("\nex 3.4.2: ")
    ex342()
    print("\nex 3.4.3: ")
    ex343()
