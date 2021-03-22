with open("sample4.txt")as f:
    data = f.read()
    if 'twinkle' in data:
        print("twinkle is present")
    else:
        print("twinkle is not present")