import random
import sys

print("""H A N G M A N
""")

words = ['python', 'java', 'kotlin', 'javascript']


def new_game():
    initial_word = random.choice(words)
    word_list = list(initial_word)
    hint = '-' * len(initial_word)
    hint_list = list(hint)
    attempts = 8
    letter_set = set()
    guesser(attempts, letter_set, hint_list, word_list, initial_word)


def char_trader(letter, word_list, hint_list):
    index = ''.join(word_list).find(letter)
    if index != -1:
        word_list[index], hint_list[index] = hint_list[index], word_list[index]
        char_trader(letter, word_list, hint_list)


def guesser(num_of_attempts, letters_set, hint_list, word_list, initial_word):
    print(f"""{''.join(hint_list)}                                                      attempts left: {num_of_attempts}
input a letter (or type \"exit\" to go back to menu):""", end='')
    letter = input()
    if letter == 'exit':
        menu()
    elif letter.isupper():
        print("Please enter a lowercase English letter")
        guesser(num_of_attempts, letters_set, hint_list, word_list, initial_word)
    elif len(letter) != 1:
        print("You should input a single letter")
        guesser(num_of_attempts, letters_set, hint_list, word_list, initial_word)
    else:
        if letter in letters_set:
            print("You've already guessed this letter")
            guesser(num_of_attempts, letters_set, hint_list, word_list, initial_word)
        else:
            letters_set.update(letter)
            if letter in ''.join(word_list):
                char_trader(letter, word_list, hint_list)
                if ''.join(hint_list) == initial_word:
                    print(f"""{initial_word}
        You guessed the word!
        You survived!""")
                    menu()
                else:
                    guesser(num_of_attempts, letters_set, hint_list, word_list, initial_word)
            else:
                print("""That letter doesn't appear in the word
                """)
                num_of_attempts -= 1
                if num_of_attempts == 0:
                    print("You lost!")
                    menu()
                else:
                    guesser(num_of_attempts, letters_set, hint_list, word_list, initial_word)


def menu():
    decision = input('''Type:
    "play" to play the game
    "exit" to quit:
    "add" if you want to add a word to the list:
    ''')
    if decision == "play":
        new_game()
    elif decision == "exit":
        sys.exit()
    elif decision == "add":
        words.append(input("write the word you want to add: \n"))
        menu()
    else:
        print("you should write either \"play\" ,\"exit\" or \"add\"")
        menu()


menu()
