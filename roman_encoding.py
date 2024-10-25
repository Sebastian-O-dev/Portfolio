code = ""

print("\\Enter = end of program\\")

while True:
    shift = input("How many +1 values are to be added to each letter in UniCode?: ")
    if shift == "":
        print("End of program")
        break
    elif shift.isdigit():
        while True:
            message = input("Enter message to be encoded by adding " + str(shift) + " to each letter in UniCode: ")

            message = message.upper().strip()
                
            if message.isalpha():
                for letter in message:
                    if letter.isalpha():
                        if letter == "Z":
                            letter = "A"
                        else:
                            letter = chr(ord(letter) + int(shift))
                        code += letter
                print(code)
                break

            else:
                print("Use only letters, try again below")
                continue
    else:
        print("Use only numbers, try again below")
        continue
