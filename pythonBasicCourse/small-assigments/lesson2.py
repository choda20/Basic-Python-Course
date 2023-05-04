def ex233():  # 2.3.3
    number_of_bricks = int(input("Enter number of bricks: "))  # assuming the input is valid
    bricks_sum = number_of_bricks // 100 + number_of_bricks % 10 + (number_of_bricks // 10) % 10
    print(str(bricks_sum))
    print(str(bricks_sum // 3))
    print(str(bricks_sum % 3))
    print(str(bricks_sum % 3 == 0))


if __name__ == '__main__':
    ex233()
