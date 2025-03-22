#key point str->ASCII: ord()
#          ASCII->str: chr()
while True:
    try:
        new_sen=""
        sentence=input()
        for i in sentence:
            new_sen+=chr(ord(i)-7)
        print(new_sen)
    except EOFError:
        pass