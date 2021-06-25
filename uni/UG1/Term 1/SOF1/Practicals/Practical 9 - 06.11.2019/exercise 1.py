a_word = "a word or maybe not so"
f = open('exo1.txt', 'w+') # opens existing, if not creates new (as denoted by +), file with file name filename, which is to be completely erased and then written in
f.write(a_word)
f.close() 

def main():
    f = open("yada.txt", "w+")

    for i in range(10):
        f.write("This is a line %d\r\n" % (i+1)) # \r\n or \n\n causes for two enters, and %d used as placeholder for decimal values (alternatively %s ditto for strings), and so (i+1) substituted into the string when being printed into the file
    
    f.close()

if __name__ == "__main__":
    main()