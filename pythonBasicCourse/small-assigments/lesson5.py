def last_early(my_str):  # 5.3.4
    if my_str[-1].lower() in my_str[:len(my_str) - 1].lower():
        print(str(True))
        return True
    print(str(False))
    return False


def distance(num1, num2, num3):  # 5.3.5
    close_to_1 = (abs(abs(num1) - abs(num2)) == 1) or (abs(abs(num1) - abs(num3)) == 1)
    far_from_2_3 = ((abs(abs(num2) - abs(num3)) >= 2) and (abs(abs(num2) - abs(num1)) >= 2)) or \
                   ((abs(abs(num3) - abs(num1)) >= 2) and (abs(abs(num3) - abs(num1)) >= 2))
    if close_to_1 and far_from_2_3:
        print(str(True))
        return True
    print(str(False))
    return False


def filter_teens(a=13, b=13, c=13):  # 5.3.6
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    print(a + b + c)
    return a + b + c


def fix_age(age):
    if age in range(13, 20):
        return 0
    else:
        return age


def chocolate_maker(small, big, x):  # 5.3.7
    pass


def ex541():  # 5.4.1
    pass


if __name__ == '__main__':
    print("ex 5.3.4: ")
    last_early("best of luck")
    print("\nex 5.3.5: ")
    distance(1, 2, 10)
    print("\nex 5.3.6: ")
    filter_teens(2, 13, 1)
    print("\nex 5.3.7: ")
    chocolate_maker()
    print("\nex 5.4.1: ")
    ex541()
