words = ["pappu","goli","gobar","kaddu"]
with open("simple@")as f:
    content = f.read()
    for word in words:
        content = content.replace(word,"good")
        with open("simple@.txte","w")as f:
            f.write(content)
