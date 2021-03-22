with open("simple.txt")as f:
    content = f.read()
    content = content.replace("pappu", "@@%$%")
    with open("simple.txt","w")as f:
        f.write(content)
