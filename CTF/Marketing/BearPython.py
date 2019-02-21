with open('Bear_Wordlist.txt','r') as input:
    with open('Output.txt', 'w') as output:
        for line in input:
            output.write(line.rstrip() + line.rstrip() + line.rstrip() + "\r\n")
