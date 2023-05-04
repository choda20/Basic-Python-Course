def ask_for_user_input(text):
    user_input = input(text).lower()
    valid_input, user_input = is_valid_input(user_input)
    print("Entered value is: " + user_input)
    return valid_input


def is_valid_input(letter_guessed):
    valid_input = True
    if not (letter_guessed.isalpha()) and (len(letter_guessed) > 1):
        letter_guessed = "E3"
        valid_input = False
    elif len(letter_guessed) > 1:
        letter_guessed = "E1"
        valid_input = False
    elif not letter_guessed.isalpha():
        letter_guessed = "E2"
        valid_input = False
    return valid_input, letter_guessed


def draw_hanged_man(man_status):
    space = " "
    if man_status == 1:
        print("x------x")
    elif man_status == 2:
        print("x------x\n|\n|\n|\n|\n|")
    elif man_status == 3:
        print(f"x------x\n|{space * 6}|\n|{space * 6}0\n|\n|\n|")
    elif man_status == 4:
        print(f"x------x\n|{space * 6}|\n|{space * 6}0\n|{space * 6}|\n|\n|")
    elif man_status == 5:
        print(f"x------x\n|{space * 6}|\n|{space * 6}0\n|{space * 5}/|\\\n|\n|")
    elif man_status == 6:
        print(f"x------x\n|{space * 6}|\n|{space * 6}0\n|{space * 5}/|\\\n|{space * 5}/\n|")
    elif man_status == 7:
        print(f"x------x\n|{space * 6}|\n|{space * 6}0\n|{space * 5}/|\\\n|{space * 5}/ \\\n|")


if __name__ == '__main__':
    HANGMAN_ASCII_ART = "Welcome to the game Hangman\n" \
                        "_    _\n| |  | |\n" \
                        "| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n" \
                        "|  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\\n" \
                        "| |  | | (_| | | | | (_| | | | | | | (_| | | | |\n" \
                        "|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n" \
                        "                     __/ |\n                 |___/ "
    MAX_TRIES = 6
    word_to_guess = ask_for_user_input("Enter a word: ")
    print("_ " * len(word_to_guess))
