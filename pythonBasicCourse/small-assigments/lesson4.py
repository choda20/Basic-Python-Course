import datetime


def ex422(): # 4.2.2
    user_input = input("Enter a string: ")
    if user_input[-1::-1].lower().replace(" ", "") == user_input[0::].lower().replace(" ", ""):
        print("OK")
    else:
        print("NOT")


def ex423(): # 4.2.3
    user_input = input("Insert the temperature you would like to convert: ").lower()  # assuming the input is valid
    temperature = float(user_input[0:len(user_input) - 1])
    if user_input.endswith("c"):
        print(str(((temperature * 9) + (32 * 5)) / 5) + "F")
    else:
        print(str(((temperature * 5) - 160) / 9) + "C")


def ex424(): # 4.2.4
    user_input = input("Enter a date: ")
    date_list = user_input.split("/")
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_num = datetime.date(int(date_list[2]), int(date_list[1]), int(date_list[0])).weekday()
    print(week_days[week_num])


if __name__ == '__main__':
    print("ex 4.2.2: ")
    ex422()
    print("\nex 4.2.3: ")
    ex423()
    print("\nex 4.2.4: ")
    ex424()
