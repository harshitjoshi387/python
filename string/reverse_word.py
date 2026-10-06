def reverse_word(s):
    words= s.split()
    words=words[: :-1]
    return(" ".join(words))


print(reverse_word("i love coding"))