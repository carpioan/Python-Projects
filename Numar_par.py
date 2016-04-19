def reverse(text):
    length = len(text)
    word = []
    while length > 0:
        word.append(text[length - 1])
        length -= 1
    return ''.join(word)

print reverse("abracadabra")