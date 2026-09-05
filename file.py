try:
    stream = open("C:\Users\User\Desktopile.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)



try:
    # Some stream operations.
except IOError as exc:
    print(exc.errno)
 