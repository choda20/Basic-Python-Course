from collections import defaultdict


def ex821():  # 8.2.1
    data = ("self", "py", 1.543)
    format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"
    print(format_string % data)


def sort_prices(list_of_tuples):  # 8.2.2
    sorted_lst = sorted(list_of_tuples, key=lambda x: x[0])
    print(sorted_lst)
    return tuple(sorted_lst)


def mult_tuple(tuple1, tuple2):  # 8.2.3
    mult_list = []
    for x in tuple1:
        for y in tuple2:
            mult_list.append((x, y))
            mult_list.append((y, x))
    print(mult_list)
    return tuple(mult_list)


def sort_anagrams(list_of_strings):  # 8.2.4
    anagram_list = defaultdict(list)
    for element in list_of_strings:
        anagram_list[str(sorted(element))].append(element)
    anagram_list = list(anagram_list.values())
    print(anagram_list)
    return anagram_list


def ex832():  # 8.3.2
    my_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970",
               "hobbies": ["Sing", "Compose", "Act"]}
    number = 0
    number = int(input("Enter a number: "))
    if number == 1:
        print(my_dict["last_name"])
    elif number == 2:
        print(".".join(my_dict["birth_date"])[1])
    elif number == 3:
        print(len(my_dict["hobbies"]))
    elif number == 4:
        print(my_dict["hobbies"][len(my_dict["hobbies"] - 1)])
    elif number == 5:
        my_dict["hobbies"] = my_dict["hobbies"] + ["Cooking"]
    elif number == 6:
        print(tuple(".".join(my_dict["birth_date"])))
    elif number == 7:
        my_dict["age"] = 19
        print(my_dict["age"])


def count_chars(my_str):  # 8.3.3
    count_dict = {}
    for char in my_str:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    print(count_dict)
    return count_dict


def inverse_dict(my_dict):  # 8.3.4
    inversed_dict = {}
    for key, value in my_dict.items():
        if value not in inversed_dict.keys():
            inversed_dict[value] = [key]
        else:
            inversed_dict[value].append(key)
    print(inversed_dict)
    return inversed_dict


if __name__ == '__main__':
    print("ex 8.2.1: ")
    ex821()
    print("\nex 8.2.2: ")
    sort_prices([('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')])
    print("\nex 8.2.3: ")
    mult_tuple((1, 2), (4, 5))
    print("\nex 8.2.4: ")
    sort_anagrams(['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                   'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts'])
    print("\nex 8.3.2: ")
    ex832()
    print("\nex 8.3.3: ")
    count_chars("abra cadabra")
    print("\nex 8.3.4: ")
    inverse_dict({'I': 3, 'love': 3, 'self.py!': 2})
