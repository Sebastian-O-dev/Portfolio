import time

print("""\nThis program will encode your message (1 word limit, please don't use white-space),\nby adding an (x) amount of +1 'shift' in value to each letter, changing it's position\nin the English alphabet by (x).\n
If you exceed the last letter of the alphabet, the coding is 'looped around' back to the\nfirst letter of the alphabet.\n
\\Enter = end of program\\\n""")

while True:
    
    shift_input = input("How many +1 'shifts' are to be done to each letter in the message?: ").strip().replace(" ", "")

    if shift_input == "26":
        print("By selecting 26 as the 'shift', you aren't encoding the message. Try again.")
        continue

    if shift_input == "":
        print("\nEnd of program.")
        break

    if shift_input.isdigit():
        shift = int(shift_input)

        while True:
            message = input(
                "Enter message to be encoded by shifting each letter by " + str(shift) + ": ").upper().strip()

            if message.isalpha():
                message_list = [ord(i) for i in message]

                unicode_list = [j + shift if j + shift <= 90
                                            else 65 + ((j + shift - 65) % 26)
                                            for j in message_list]

                print("Your coded message: " + "".join(chr(k) for k in unicode_list) + "\n")
                time.sleep(2)
                
                print("\n!New word for encoding! \n\\to stop the program press Enter\\\n")
                break
            
            else:
                    print("Use only letters, try again below")
                    continue

    else:
        print("Use only a single number composed of one or more digits, try again below")
        continue
