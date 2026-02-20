inp = "Python is very very easy language"
out = [(word.lower(), len(word)) for word in inp.split()]
print(out)

inp1 = "Hello WorLD"
out1 = {char: ord(char) for char in inp1 if char.isupper()}
print(out1)