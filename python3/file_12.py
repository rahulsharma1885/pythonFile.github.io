with open("simple.txt")as f:
    content = f.read()
    content = content.replace("rahul","@#$%%^")
    with open("simple.txt", "w")as f:
        f.write(content)