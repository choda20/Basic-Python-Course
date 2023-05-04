def shift_left(my_list):  # 6.1.2
    new_list = my_list[1::] + [my_list[0]]
    print(str(new_list))
    return new_list


def format_list(my_list):  # 6.2.3
    list_string = ', '.join(my_list[0:len(my_list) - 1:2]) + ", and " + my_list[-1]
    print(list_string)
    return list_string


def extend_list_x(list_x, list_y):  # 6.2.4
    list_x = [*list_y, *list_x]
    print(list_x)
    return list_x


def are_lists_equal(list1, list2):  # 6.3.1
    if sorted(list1) == sorted(list2):
        print(str(True))
        return True
    print(str(False))
    return False


def longest(my_list):  # 6.3.2
    print(max(my_list, key=len))
    return max(my_list, key=len)


if __name__ == '__main__':
    print("ex 6.1.2: ")
    shift_left([1, 2, 3])
    print("\nex 6.2.3: ")
    format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"])
    print("\nex 6.2.4: ")
    extend_list_x([4, 5, 6], [1, 2, 3])
    print("\nex 6.3.1: ")
    are_lists_equal([0.6, 1, 2, 3], [3, 2, 0.6, 1])
    print("\nex 6.3.2: ")
    longest(["111", "234", "2000", "goru", "birthday", "09"])
    print("\nex 6.2.4: ")
