import random

def word_random():
    words = ["elefant", "electrocentrala", "biserica", "binecuvantare", "spanzuratoare", "masina", "cravata"]
    word = words[random.randint(0, len(words)-1)]
    return word

def show_word(word):
    for character in word:
        print character + " ",
    print("")

def get_guess():
    print "Introdu o litera: "
    return raw_input() #pot incerca aici sa scot print

def process_letter(letter, secret_word, blanked_word):
    result = False

    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blanked_word[i] = letter

    return result

def print_incercari(numar_de_incercari):
    for i in range(0, numar_de_incercari):
        print "X",
    print ("")

def play_spanzuratoarea():
    incercari = 0
    max_incercari = 6
    playing = True

    word = word_random()
    blanked_word = list("_" * len(word))

    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)

        if not found:
            incercari += 1
            print_incercari(incercari)

        if incercari >= max_incercari:
            playing = False

        if not "_" in blanked_word:
            playing = False

    if incercari >= max_incercari:
        print "Ai pierdut!"
    else:
        print "Ai castigat!"

print "Jocul a inceput."
play_spanzuratoarea()
print "Jocul s-a incheiat."