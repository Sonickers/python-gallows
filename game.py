import random

def choose_word(words_list):
    words_index = random.randint(0, len(words_list) - 1)
    return words_list[words_index]


def game_board(miss_turn, hit_turn, chosen_word):
    print('Missed letters:', end='')
    for letter in miss_turn:
        print(letter, end='')
    print()

    empty_places = '_' * len(chosen_word)

    for i in range(len(chosen_word)):
        if chosen_word[i] in hit_turn:
            empty_places = empty_places[:i] + chosen_word[i] + empty_places[i+1:]

    for letter in empty_places:
        print(letter, end=' ') 


def try_letter(already_added):
    while True:
        print('Write letter:')
        turn = input()
        turn = turn.lower()
        if len(turn) != 1:
            print('Just one letter!')
        elif turn in already_added:
            print('Again? Give me another one!')
        elif turn not in 'abcdefghijklmnoprstuvwxyz':
            print('Just letters please')
        else:
            return turn


words = 'anaconda ant bat deer fox mouse rabbit crow duck owl robin spider swan frog snake horse elephant dog cat goat sheep pig cow'.split()

print("WELCOME TO GALLOWS!")
miss_turn = ' '
hit_turn = ' '
chosen_word = choose_word(words)
print(chosen_word)