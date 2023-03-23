while(True):
    try:
        string = input().rstrip()
        print(string)
    except EOFError:
        break