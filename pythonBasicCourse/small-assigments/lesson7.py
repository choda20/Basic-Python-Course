from collections import OrderedDict


def squared_numbers(start, stop):  # 7.1.4
    squared_list = []
    while start <= stop:
        squared_list.append(start ** 2)
        start += 1
    print(squared_list)
    return squared_list


def is_greater(my_list, n):  # 7.2.1
    new_list = []
    for element in my_list:
        if element > n:
            new_list.append(element)
    print(new_list)
    return element


def numbers_letters_count(my_str):  # 7.2.2
    number_count = 0
    other_count = 0
    for element in my_str:
        if element.isdigit():
            number_count += 1
        else:
            other_count += 1
    count_list = [number_count, other_count]
    print(count_list)
    return count_list


def seven_boom(end_number):  # 7.2.4
    boom_list = []
    for i in range(1, end_number + 1):
        if i % 7 == 0 or '7' in str(i):
            boom_list.append("BOOM")
        else:
            boom_list.append(i)
    print(boom_list)
    return boom_list


def sequence_del(my_str):  # 7.2.5
    no_dups = "".join(OrderedDict.fromkeys(my_str))
    print(no_dups)
    return no_dups


def ex726():  # 7.2.6
    shopping_string = input("Enter shopping list: ")
    shopping_list = ",".join(shopping_string)
    number = 0
    while number != 9:
        if number == 1:
            print(shopping_list)
        elif number == 2:
            print(len(shopping_list))
        elif number == 3:
            product_name = input("Enter product name: ")
            if product_name in shopping_list:
                print("Product is in list.")
            else:
                print("Product is not in list")
        elif number == 4:
            product_name = input("Enter product name: ")
            print(product_name + " appears in the list: " + shopping_list.count(product_name) + " times")
        elif number == 6:
            product_name = input("Enter product name: ")
            shopping_list.append(product_name)
        elif number == 7:
            for product in shopping_list:
                if len(product) < 3 or not product.isalpha():
                    print(product, end=" ")
        elif number == 8:
            shopping_list = list(OrderedDict.fromkeys(shopping_list))
        elif number == 5:
            product_name = input("Enter product name: ")
            shopping_list.remove(product_name)
        number = input("Enter a number: ")


def arrow(my_char, max_length):  # 7.2.7
    arrow_string = ""
    for i in range(1, max_length + 1):
        arrow_string += i * my_char + "\n"
    for i in range(max_length-1, 0,-1):
        arrow_string += i * my_char + "\n"
    print(arrow_string)
    return arrow_string


if __name__ == '__main__':
    print("ex 7.1.4: ")
    squared_numbers(-3, 3)
    print("\nex 7.2.1: ")
    is_greater([1, 30, 25, 60, 27, 28], 28)
    print("\nex 7.2.2: ")
    numbers_letters_count("Python 3.6.3")
    print("\nex 7.2.4: ")
    seven_boom(17)
    print("\nex 7.2.5: ")
    sequence_del("ppyyyyythhhhhooonnnnn")
    print("\nex 7.2.6: ")
    ex726()
    print("\nex 7.2.7: ")
    arrow('* ', 5)
