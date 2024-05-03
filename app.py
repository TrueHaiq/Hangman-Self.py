from pyfiglet import figlet_format

hangman_states = [
'''
x-------x
|
|
|
|
|
''',
'''
x-------x
|       |
|       0
|
|
|
''',
'''
x-------x
|       |
|       0
|       |
|
|
''',
'''
x-------x
|       |
|       0
|      /|
|
|
''',
'''
x-------x
|       |
|       0
|      /|\\
|
|
''',
'''
x-------x
|       |
|       0
|      /|\\
|      /
|
''',
'''
x-------x
|       |
|       0
|      /|\\
|      / \\
|
'''
]

def get_hangman_state(stateId):
    return hangman_states[stateId]


iso_text = figlet_format("HANGMAN", font="slant") # isometric1

HANGMAN_ASCII_ART = f"""
--------------------------------------------------------\n
Welcome to the Hangman game!
{iso_text}
"""

MAX_RETRIES = 6

def get_intro(fail_count):
    lives_count = MAX_RETRIES-fail_count

    caption = HANGMAN_ASCII_ART
    caption += "Lives: "+ str(lives_count)
    
    return caption

def get_word():
    word = ' '
    while(' ' in word):
        word = input("Please enter one word: ")

    guessed_word = ''.join(['_ ' for i in range(len(word))])

    print(guessed_word)
    
def is_valid_input(letter_guessed, old_letters_guessed):
    isE1 = len(letter_guessed) > 1
    isE2 = not letter_guessed.isalpha()
    letter_exists = letter_guessed in old_letters_guessed

    if(isE1 or isE2 or letter_exists):
        return False
    
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    is_valid = is_valid_input(letter_guessed, old_letters_guessed)

    if(is_valid):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        letters = ''.join([ltr+" -> " for ltr in old_letters_guessed[:-1]])
        if(len(old_letters_guessed)>0): letters += old_letters_guessed[-1]

        print("X")
        print("Guessed Letters:", letters)
        return False

def get_hidden_word(secret_word, old_letters_guessed):
    secret_caption_arr = [ltr if ltr in old_letters_guessed else "_" for ltr in secret_word]
    secret_caption = ' '.join(secret_caption_arr)

    return secret_caption

def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def choose_word(file_path, index):
    with open(file_path, 'r') as f:
        words = f.read().split()

        unique_words = remove_duplicates_preserve_order(words)
        unique_words_len = len(unique_words)
        selected_word = unique_words[(index - 1) % unique_words_len]

    return unique_words_len, selected_word.lower()

def check_win(secret_word, old_letters_guessed):
    secret_word_set = set(secret_word)
    old_letters_set = set(old_letters_guessed)

    return old_letters_set.issuperset(secret_word_set)


def main():
    fail_count = 0
    intro = get_intro(fail_count)
    print(intro)

    file_path = input("Enter words text file path: ")
    index = int(input("Enter word index (min 1): "))
    
    (words_count, secret_word) = choose_word(file_path, index)

    print("\nLet's start!")

    old_letters_guessed = []
    is_win = False
    while(fail_count < MAX_RETRIES and not is_win):
        hidden_word = get_hidden_word(secret_word, old_letters_guessed)

        print(hidden_word)

        is_valid = False
        while(not is_valid):
            letter_guessed = input("\nGuess a letter: ").lower()
            is_valid = try_update_letter_guessed(letter_guessed, old_letters_guessed)

        if(letter_guessed not in secret_word):
            fail_count+=1
            hangman_state = get_hangman_state(fail_count)

            print("Wrong :(")
            print(hangman_state)

        is_win = check_win(secret_word, old_letters_guessed)
    
    if(is_win): print("\nWIN!")
    else: print("\nLOSE!")
    print("Secret Word:", secret_word)
    print(f"Total Fails: {fail_count}/{MAX_RETRIES}")

if __name__ == "__main__":
    main()
