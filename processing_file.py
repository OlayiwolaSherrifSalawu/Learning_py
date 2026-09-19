stream = open('file.txt', 'rt', encoding='utf-8')
for line in open("file", "rt"):
    for char in line:
        if char.lower() not in "aeiouy ":
            print(char, end='')