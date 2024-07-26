import random
import string

WORDLIST_FILENAME = ""


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, "r")
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()


def print_word_with_dashs(inp, n):
    li = []

    for i in range(0, len(inp)):
        if i in n:
            li.append(inp[i])
        else:
            li.append("_ ")

    return " ".join(li)


def hangman(guesses=3):
    word = random.choice(wordlist)
    spaces = "-" * 25
    print(f"{spaces} G A M E  S T A R T E D {spaces} \n")

    hints = int(
        input("choose the leve:   EASY(3)     MEDIUM(2)     HARD(1)\nchoose number: ")
    )

    if hints == 3:
        num_hints = round(len(word) / 2)
    elif hints == 2:
        num_hints = round(len(word) / 4)
    else:
        num_hints = 0

    random_recommender = random.sample(range(len(word)), num_hints)

    inp = input(
        f"{print_word_with_dashs(word, random_recommender)}\nEnter your guess (word of {len(word)} characters): "
    ).lower()
    output = ("_ " * len(word)).split(" ")[:-1]

    while guesses != 1:
        if inp == word:
            print("Y O U  W O N")
            break

        if len(inp) != len(word):
            inp = input(f"Please Enter {len(word)} characters: ")

        if len(inp) == len(word):
            guesses -= 1
            for i in range(len(inp)):
                if word[i] == inp[i] and output[i] == "_":
                    output[i] = word[i]

            inp = input(" ".join(output) + ": \n")

    else:
        print(f"\nG A M E  O V E R \nY O U  L O S E\nthe word is: {word}")

    return "Done"


guesses = int(input("Enter the amount of guesses you want: \n"))
print(guesses)
