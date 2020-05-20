

print("\nHi, welcome to the text analyser programme. \n\nPlease log in:")

def main():
    oddelovac = "=" * 60

    print(oddelovac)
    login = input("Your nickname: ")
    print(oddelovac)
    password = input("Your password: ")
    print(oddelovac)

    if credentials(login, password):
        print(oddelovac)
        select_text = int(input("We have three texts to be analyzed.\nChoose the text by typing a number from 1 to 3:"))
        print(oddelovac)
        choose_text(select_text)
        words = str(choose_text(select_text))
        interpunctionless = str(words.strip(","))
        no_dots = str(interpunctionless.strip(".'="))
        number_words = no_dots.split()
        stats(number_words)
        print(oddelovac)

    else:
        main()

def credentials(login, password):
    registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
    n = 0
    for i, p in registered_users.items():
        n += 1
        if i == login and p == password:
            print("You are successfully logged in!")
            return True

        elif (n >= len(registered_users)):
            print("Your credentials are not correct. Please try it again.")
            return False

        else:
            pass


def choose_text(select_text):
    with open("task_template.py", "r") as TEXT:
        three_texts = TEXT.read()
        return three_texts.split("\n\n")[select_text - 1]


def stats(number_words):
    total_words = []
    numbers = []
    oddelovac = "=" * 60

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


    print(f"This text includes {all_words} words in total.\n"
          f"This text includes {all_numbers} numeric strings.\n"
          f"This text includes {title_words} title case words.\n"
          f"This text includes {smaller_words} lowercase words.\n"
          f"This text includes {upper_words} uppercase words. ")

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

    print(oddelovac)
    print(f"One letter word is in the text {letter1}x\n"
          f"Two letter word is in the text {letter2}x\n"
          f"Three letter word is in the text {letter3}x\n"
          f"Four letter word is in the text {letter4}x\n"
          f"Five letter word is in the text {letter5}x\n"
          f"Six letter word is in the text {letter6}x\n"
          f"Seven letter word is in the text {letter7}x\n"
          f"Eight letter word is in the text {letter8}x\n"
          f"Nine letter word is in the text {letter9}x\n"
          f"Ten letter word is in the text {letter10}x\n"
          f"Eleven letter word is in the text {letter11}x\n"
          f"Twelve letter word is in the text {letter12}x\n"
          f"Thirteen letter word is in the text {letter13}x\n"
          )

    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
        total_numbers = sum(map(int, numbers))

    print(oddelovac)
    print(f"The sum of all numbers in this text is: {total_numbers} ")


main()
