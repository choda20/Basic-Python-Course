def ex912():  # 9.1.2
    file_path = input("Enter text file path: ")
    action = int(input("Enter action number: "))
    if action == 1:  # sort
        reverse_string = []
        with open(file_path, "r") as text:
            lines = text.readlines()
            for line in lines:
                line_words = line.split(" ")
                for word in line_words:
                    reverse_string.append(word)
        reverse_string = sorted(set(reverse_string))
        print(reverse_string)
    elif action == 2:  # rev
        reverse_string = ""
        with open(file_path, "r") as text:
            lines = text.readlines()
            for line in lines:
                reverse_string += line.replace("\n", "")[::-1]
                reverse_string += "\n"
        print(reverse_string)
    elif action == 3:  # last
        n = int(input("Enter number: "))
        file_text = ""
        with open(file_path, "r") as text:
            file_text = text.readlines()[-n:]
        for line in file_text:
            print(line.strip())


def are_files_equal(file1, file2):  # 9.1.1
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1.strip() != line2.strip():
                print(str(False))
                return False
        if f1.readline() != f2.readline():
            print(str(False))
            return False
    print(str(True))
    return True


def copy_file_content(source, destination):  # 9.2.2
    with open(source, 'r') as f1, open(destination, 'w') as f2:
        for line in f1:
            f2.write(line)


def who_is_missing(file_name):  # 9.2.3
    found = open("found.txt", "w")
    count = 1
    with open(file_name, "r") as f1:
        lines = f1.readlines()
        numbers = ",".join(lines).split(",")
    numbers.sort()
    print(numbers)
    for number in numbers:
        if int(number) != count:
            found.write(str(count))
            break
        count += 1
    print("missing number is: " + str(count))


def my_mp3_playlist(file_path):  # 9.3.1
    longest_song_length = 0
    longest_song_name = ""
    performer_count = {}
    count = 0
    with open(file_path, "r") as playlist:
        lines = playlist.readlines()
        for line in lines:
            count += 1
            song_details = line.split(";")
            song_length = float(song_details[2].replace(":", "."))
            if song_length > longest_song_length:
                longest_song_length = song_length
                longest_song_name = song_details[0]

            if song_details[1] in performer_count.keys():
                performer_count[song_details[1]] = performer_count[song_details[1]] + 1
            else:
                performer_count[song_details[1]] = 0
    performs_most = max(performer_count, key=performer_count.get)
    results = tuple([longest_song_name, count, performs_most])
    print(results)
    return results


def my_mp4_playlist(file_path, new_song):  # 9.3.2
    with open(file_path, "a+") as playlist:
        playlist.seek(0)
        lines = playlist.readlines()
        line_count = len(lines)
        if line_count < 3:
            lines_to_add = 3 - line_count
            playlist.seek(0, 2)
            for i in range(1, lines_to_add):
                playlist.write("\n")
            playlist.write(new_song)
        else:
            lines[2] = lines[2].split(";")
            lines[2][0] = new_song
            lines[2] = ";".join(lines[2])
    with open(file_path, "w") as playlist:
        playlist.writelines(lines)


if __name__ == '__main__':
    print("ex 9.1.1: ")
    are_files_equal("text.txt", "text2.txt")
    print("\nex 9.1.2: ")
    ex912()
    print("\nex 9.2.2: ")
    copy_file_content("text.txt", "text2.txt")
    print("\nex 9.2.3: ")
    who_is_missing("text2.txt")
    print("\nex 9.3.1: ")
    my_mp3_playlist("mp3Playlist.txt")
    print("\nex 9.3.2: ")
    my_mp4_playlist("mp4Playlist.txt", "Love Story(Taylor's Version)")
