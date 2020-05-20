def main():
    oddelovac = "=" * 40

    print(oddelovac)
    print("Hi, welcome to the text analyser programme. \nPlease log in:")
    print(oddelovac)

    login = input("Please enter your nickname: ")
    password = input("Please enter your password: ")
    print(oddelovac)
    credentials(login, password)
    select_text = int(input("We have three texts to be analyzed.\nEnter a number between 1 and 3:"))
    print(oddelovac)
    choose_text(select_text)
    words = str(choose_text(select_text))
    interpunctionless = str(words.strip(","))
    no_dots = str(interpunctionless.strip(".'="))
    number_words = no_dots.split()
    stats(number_words)
    print(oddelovac)


def credentials(login, password):
    registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
    n = 0
    for i, p in registered_users.items():
        n += 1
        if i == login and p == password:
            print("You are successfully logged in!")
            break
        elif (n >= len(registered_users)):
            print("Your credentials are not correct.")
            break
        else:
            pass


def choose_text(select_text):
    with open("task_template.py", "r") as TEXT:
        three_texts = TEXT.read()
        return three_texts.split("\n\n")[select_text - 1]


def stats(number_words):
    total_words = []
    numbers = []

    for i in number_words:
        if i.isnumeric():
            numbers.append(i)

        else:
            total_words.append(i)

    title = []
    upper = []
    smaller = []

    for a in total_words:
        if a.istitle():
            title.append(a)

        elif a.isupper():
            upper.append(a)

        else:
            smaller.append(a)

    all_words = len(total_words)
    all_numbers = len(numbers)

    smaller_words = len(smaller)
    title_words = len(title)
    upper_words = len(upper)

    print(f"There are {all_words} words in the selected text.\n"
          f"There are {all_numbers} numeric strings.\n"
          f"There are {title_words} title case words.\n"
          f"There are {smaller_words} lowercase words.\n"
          f"There are {upper_words} uppercase words. ")

    print(total_words)

    letter1 = 0
    letter2 = 0
    letter3 = 0
    letter4 = 0
    letter5 = 0
    letter6 = 0
    letter7 = 0
    letter8 = 0
    letter9 = 0
    letter10 = 0
    letter11 = 0
    letter12 = 0
    letter13 = 0

    for letter in total_words:

        if len(letter) == 1:
            letter1 += 1

        elif len(letter) == 2:
            letter2 += 1

        elif len(letter) == 3:
            letter3 += 1

        elif len(letter) == 4:
            letter4 += 1

        elif len(letter) == 5:
            letter5 += 1

        elif len(letter) == 6:
            print(len(letter))
            letter6 += 1

        elif len(letter) == 7:
            letter7 += 1

        elif len(letter) == 8:
            letter8 += 1

        elif len(letter) == 9:
            letter9 += 1

        elif len(letter) == 10:
            letter10 += 1

        elif len(letter) == 11:
            letter11 += 1

        elif len(letter) == 12:
            letter12 += 1

        elif len(letter) == 13:
            letter13 += 1
        else:
            pass

    print(f"1 letter word is in the text {letter1}x\n"
          f"2 letter word is in the text {letter2}x\n"
          f"3 letter word is in the text {letter3}x\n"
          f"4 letter word is in the text {letter4}x\n"
          f"5 letter word is in the text {letter5}x\n"
          f"6 letter word is in the text {letter6}x\n"
          f"7 letter word is in the text {letter7}x\n"
          f"8 letter word is in the text {letter8}x\n"
          f"9 letter word is in the text {letter9}x\n"
          f"10 letter word is in the text {letter10}x\n"
          f"11 letter word is in the text {letter11}x\n"
          f"12 letter word is in the text {letter12}x\n"
          f"13 letter word is in the text {letter13}x\n"
          )

    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
        total_numbers = sum(map(int, numbers))

    print(f"If we sum all the numbers in this text, we would get : {total_numbers} ")

# 7 Program spočítá součet všech čísel v textu
main()