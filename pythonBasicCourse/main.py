import os.path


def choose_word(file_path, index):
    words_file = open(file_path, "r")
    words = list(set(words_file.read().split(" ")))
    return words[(index % len(words))]


def get_words_file():
    valid_path = False
    file_path = ""
    while not valid_path:
        file_path = input("Enter word file path: ")
        if os.path.exists(file_path) and file_path.endswith(".txt"):
            valid_path = True
        else:
            print("Invalid path, try again.\n")
    return file_path


def get_word_index():
    index = 0
    valid_word = False
    print()
    while not valid_word:
        index = input("Enter a random positive number: ")
        if index.isdigit() and int(index) > 0:
            index = int(index)
            valid_word = True
        else:
            print("Invalid number, try again.\n")
    return index


def get_letter_from_user(guessed_letters):
    user_input = input("\nEnter a letter: ").lower()
    valid_input = try_update_letter_guessed(user_input, guessed_letters)
    while not valid_input:
        user_input = input("\nEnter a letter: ").lower()
        valid_input = try_update_letter_guessed(user_input, guessed_letters)
    return user_input


def check_valid_input(letter_guessed, old_letters_guessed):
    valid_input = True
    if (not (letter_guessed.isalpha())) and (len(letter_guessed) > 1):
        valid_input = False
    return valid_input


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    valid_letter = check_valid_input(letter_guessed, old_letters_guessed)
    if valid_letter and letter_guessed not in old_letters_guessed:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(*old_letters_guessed, sep=" -> ")
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    word_guessed = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word_guessed += letter + " "
        else:
            word_guessed += "_ "
    return word_guessed


def check_win(secret_word, old_letters_guessed):
    word_guessed = show_hidden_word(secret_word, old_letters_guessed)
    if word_guessed.strip().replace(" ", "") == secret_word:
        return True
    return False


def print_hangman(num_of_tries):
    if num_of_tries in HANGMAN_PHOTOS.keys():
        print(HANGMAN_PHOTOS[num_of_tries])
    else:
        print("Invalid number of tries")


def init_hangman_dict():
    space = " "
    hangman_ascii_dict = {
        1: "x------x",
        2: "x------x\n|\n|\n|\n|\n|",
        3: f"x------x\n|{space * 6}|\n|{space * 6}0\n|\n|\n|",
        4: f"x------x\n|{space * 6}|\n|{space * 6}0\n|{space * 6}|\n|\n|",
        5: f"x------x\n|{space * 6}|\n|{space * 6}0\n|{space * 5}/|\\\n|\n|",
        6: f"x------x\n|{space * 6}|\n|{space * 6}0\n|{space * 5}/|\\\n|{space * 5}/\n|",
        7: f"x------x\n|{space * 6}|\n|{space * 6}0\n|{space * 5}/|\\\n|{space * 5}/ \\\n|"
    }
    return hangman_ascii_dict


def print_welcome_text():
    HANGMAN_ASCII_ART = "Welcome to the game Hangman\n" \
                        "_    _\n| |  | |\n" \
                        "| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n" \
                        "|  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\\n" \
                        "| |  | | (_| | | | | (_| | | | | | | (_| | | | |\n" \
                        "|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n" \
                        "                     __/ |                        \n" \
                        "                    |___/ \n"
    print(HANGMAN_ASCII_ART)


def print_results(secret_word, old_letters_guessed):
    if check_win(secret_word, old_letters_guessed):
        print("\nGame Results: YOU WON!")
    else:
        print("\nGame Results: YOU LOST!")


if __name__ == '__main__':
    print_welcome_text()

    MAX_TRIES = 7
    num_of_tries = 1
    old_letters_guessed = []
    HANGMAN_PHOTOS = init_hangman_dict()
    WORD_FILE = get_words_file()
    word_index = get_word_index()
    secret_word = choose_word(WORD_FILE, word_index)
    entered_letter = ""
    
    print("\nStarting The Game!\n")
    print_hangman(num_of_tries)
    print("\n" + show_hidden_word(secret_word, old_letters_guessed))
    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        entered_letter = get_letter_from_user(old_letters_guessed)

        if entered_letter not in secret_word:
            num_of_tries += 1
            print("\nEntered letter is not in the secret word :(")
            print(str(MAX_TRIES - num_of_tries) + " tries left.\n")
            print_hangman(num_of_tries)
        print("\n" + show_hidden_word(secret_word, old_letters_guessed))

    print_results(secret_word, old_letters_guessed)
