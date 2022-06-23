#========FURRO404========#
#PassGen.py
#Generate a string of random chars using ASCII
import random
#----------------#
special_chars = [33, 35, 36, 37, 38, 63, 64]

while True:
    x = 0
    amount_of_passwords = int(input("How many passwords would you like? "))
    amount_of_chars =  int(input("How many characters would you like the password to be? "))
                           
    for password in range(0, amount_of_passwords):
        combination = []
        for chars in range(0, amount_of_chars):
            type_of_char = random.randint(0, 3)

            if type_of_char == 0:
                RandomChar = str(chr(random.randint(65,90)))
            
            elif type_of_char == 1:
                RandomChar = str(chr(random.randint(97,122)))

            elif type_of_char == 2:
                RandomChar = str(chr(random.randint(48,57)))
                
            elif type_of_char == 3:
                RandomChar = str(chr(random.choice(special_chars)))
                
            combination.append(RandomChar)

        x = x + 1
        password = ''.join(combination)
        print(f"Password {x}: {password}")
        
    print("\n\n")
#========FURRO404========#
