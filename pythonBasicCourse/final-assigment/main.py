import os.path


def choose_word(file_path, index):
    '''
    function that returns the word in the index location from
    the file pointed at by file_path
    :param file_path: the path of a text file
    :param index: index of a random word
    :return: a random word from the text file
    '''
    words_file = open(file_path, "r")
    words = list(set(words_file.read().split(" ")))
    return words[(index % len(words))]


def get_words_file():
    '''
    function that a path to a text file from the user,
    if the path is valid (the file exists and is of type .txt) the path
    is returned, otherwise the user will be asked to enter a new path
    :return: path of a text file
    '''
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
    '''
    function that gets a string as an input, if the input is
    a positive number it is returned as an integer, otherwise the user
    is asked to enter a new string
    :return: a number
    '''
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
    '''
    function that gets a string the user would like to guess, if the string
    is a single letter it is returned, otherwise the user will be asked to
    enter a new string
    :param guessed_letters: list of letters that were already entered by the user
    :return: a letter entered by the user that is not a part of guessed_letters
    '''
    user_input = input("\nEnter a letter: ").lower()
    valid_input = try_update_letter_guessed(user_input, guessed_letters)
    while not valid_input:
        user_input = input("\nEnter a letter: ").lower()
        valid_input = try_update_letter_guessed(user_input, guessed_letters)
    return user_input


def check_valid_input(letter_guessed):
    '''
    function that checks if a string is a single letters, and returns a boolean
    accordingly.
    :param letter_guessed: the string to be checked
    :return: true if the string is a single letter, false otherwise
    '''
    valid_input = True
    if not (letter_guessed.isalpha() and len(letter_guessed) == 1):
        valid_input = False
    return valid_input


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    '''
    function that deals with a valid letter. if the letter is new, it is
    added to old_letters_guessed, otherwise all guessed letters so far are
    printed
    :param letter_guessed: a letter the user entered
    :param old_letters_guessed: list of guessed letters
    :return: true if the letter is new, false otherwise
    '''
    valid_letter = check_valid_input(letter_guessed)
    if valid_letter and letter_guessed not in old_letters_guessed:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("\nX, invalid input.")
        if len(old_letters_guessed) > 0:
            print("entered letters so far:", end=" ")
            print(*old_letters_guessed, sep=" -> ")
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    '''
    returns the hidden word only showing already guessed letters
    :param secret_word: the word to be printed
    :param old_letters_guessed: letters the user guessed (meaning they
     can be printed)
    :return: secret_word where all non guessed letters are replaced with "_"
    '''
    word_guessed = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word_guessed += letter + " "
        else:
            word_guessed += "_ "
    return word_guessed


def check_win(secret_word, old_letters_guessed):
    '''
    checks if the player has guessed the secret_word
    :param secret_word: the word to be guessed
    :param old_letters_guessed: letters the user guessed
    :return: true if the user has won(guessed all the letters forming secret_word),
    otherwise false
    '''
    word_guessed = show_hidden_word(secret_word, old_letters_guessed)
    if word_guessed.strip().replace(" ", "") == secret_word:
        return True
    return False


def print_hangman(num_of_tries):
    '''
    prints the hangman based on the provided stage
    :param num_of_tries: the stage of the hangman
    :return: none
    '''
    if num_of_tries in HANGMAN_PHOTOS.keys():
        print(HANGMAN_PHOTOS[num_of_tries])
    else:
        print("Invalid number of tries")


def init_hangman_dict():
    '''
    creates the hangman dictionary, where in each stage(ascii drawing) is
    represented by a number going from 1(starting stage) to 7(complete)
    :return: the hangman dictionary
    '''
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
    '''
    prints the welcome text to the program
    :return: none
    '''
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
    '''
    prints the results of the game based on the value provided by check_win
    :param secret_word: the word to be guessed
    :param old_letters_guessed: letters guessed
    :return: none
    '''
    if check_win(secret_word, old_letters_guessed):
        print("\nGame Results: YOU WON!")
    else:
        print("\nGame Results: YOU LOST!")


if __name__ == '__main__':
    '''
    main function
    '''
    print_welcome_text()

    MAX_TRIES = 7  # maximum number of guesses
    num_of_tries = 1  # current number of guesses
    old_letters_guessed = []  # list of guessed letters
    HANGMAN_PHOTOS = init_hangman_dict()  # dictionary containing all ascii drawings of the hangman by stage
    WORD_FILE = get_words_file()  # path to the text file
    word_index = get_word_index()  # index of the chosen word inside the text file
    secret_word = choose_word(WORD_FILE, word_index)  # the word to be guessed by the player
    entered_letter = ""  # will hold the letters the player enters

    print("\nStarting The Game!\n")
    print_hangman(num_of_tries)
    print("\n" + show_hidden_word(secret_word, old_letters_guessed))
    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):  # main game loop, goes on as
        # long as the current number of wrong guesses < allowed wrong guesses and the player has yet to win

        entered_letter = get_letter_from_user(old_letters_guessed)  # asks the user for input and validates it

        if entered_letter not in secret_word:  # letter is not a part of the word to guess
            num_of_tries += 1
            print("\nEntered letter is not in the secret word :(")
            print(str(MAX_TRIES - num_of_tries) + " tries left.\n")
            print_hangman(num_of_tries)
        print("\n" + show_hidden_word(secret_word,
                                      old_letters_guessed))  # prints the players progress in guessing the word

    print_results(secret_word, old_letters_guessed)
