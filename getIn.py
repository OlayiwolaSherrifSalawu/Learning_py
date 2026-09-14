stream = open("text.txt")
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
stream.close()



from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

from os import strerror

try:
	file = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
    