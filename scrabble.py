
def cens(word):
    total = 0
    for letter in word:
        total += score[letter]
    return total

print scrabble_score("hidrocentrala")


