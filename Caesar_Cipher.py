#=========FURRO404=========#
#Caesar_Cipher.py
import random
#----------------#
def Text_Deconstructor(text):
    L_text = []
    L_text = text.split(" ")
    text = L_text
    return text

def encrypt(text, s):
    Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Alphabet_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    Punctuation = ['!', '?', ',', '.', ' ']
    encrypted = ""
    
    if s == "":
        s = random.randint(1, 25)
    else:
        s = int(s)
    process = "unfinished"
    x = 0
    y = 0
    
    while process == "unfinished":
        if len(encrypted) == len(text):
            process = "finished"
        elif Alphabet[x] == text[y]:
            encrypted += (Alphabet[x+s])
            y = y + 1
            x = 0
        elif Alphabet_lower[x] == text[y]:
            encrypted += (Alphabet_lower[x+s])
            y = y + 1
            x = 0
        elif text[y] in Punctuation: #Its punctuation
            encrypted += text[y]
            y = y + 1
            x = 0
        elif text[y] in Numbers:
            encrypted += text[y]
            y = y + 1
            x = 0
        else:
            x = x + 1

    print ("\n\n\nPlain Text : " + text)
    print ("Shift pattern : " + str(s))
    print ("Cipher: " + encrypted + "\n\n\n")



def decrypt(text, s):
    Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Alphabet_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    Punctuation = ['!', '?', ',', '.', ' ']
    decrypted = ""
    
    if s != "":
        x = 0
        y = 0
        s = int(s)
        process = "unfinished"
        decrypted = ''
        
        while process == "unfinished":
            if len(decrypted) == len(text):
                process = "finished"
            elif Alphabet[x] == text[y]:
                decrypted += (Alphabet[x-s])
                y = y + 1
                x = 0
            elif Alphabet_lower[x] == text[y]:
                decrypted += (Alphabet_lower[x-s])
                y = y + 1
                x = 0
            elif text[y] in Punctuation:
                decrypted += text[y]
                y = y + 1
                x = 0
            elif text[y] in Numbers:
                decrypted += text[y]
                y = y + 1
                x = 0
            else:
                x = x + 1
        print("\nShift pattern", str(s), ":", decrypted)
        
    else: #decrypt without key
        iteration = 0
        for i in range(1, 26):
            x = 0
            y = 0
            process = "unfinished"
            iteration += 1
            decrypted = ''
            
            while process == "unfinished":
                if len(decrypted) == len(text):
                    process = "finished"
                elif Alphabet[x] == text[y]:
                    decrypted += (Alphabet[x-iteration])
                    y = y + 1
                    x = 0
                elif Alphabet_lower[x] == text[y]:
                    decrypted += (Alphabet_lower[x-iteration])
                    y = y + 1
                    x = 0
                elif text[y] in Punctuation:
                    decrypted += text[y]
                    y = y + 1
                    x = 0
                elif text[y] in Numbers:
                    decrypted += text[y]
                    y = y + 1
                    x = 0
                else:
                    x = x + 1
            print("\nShift pattern", str(iteration), ":", decrypted)
    
    
while True:
    command = int(input("\n\n\n1 ~ Encryption\n2 ~ Decryption\nEnter number for command: "))
    
    if command == 1:
        text = str(input("Enter message to encrypt: "))
        s = input("Press enter for a random shift or type your custom shift: ")
        Text_Deconstructor(text)
        encrypt(text, s)
        
    if command == 2:
        text = str(input("Enter encrypted text: "))
        s = input("Press enter if you dont know the shift, else type it here: ")
        Text_Deconstructor(text)
        decrypt(text, s)
#=========FURRO404=========#
