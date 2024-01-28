from caesar_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b',
 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(plain_direction, plain_text, plain_shift):
    listt = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            if plain_direction == "encode":
                new_position = position + plain_shift
            elif plain_direction == "decode":
                new_position = position - plain_shift
            word = alphabet[new_position]
            listt += word
        else:
            listt += char

    print(f"The {plain_direction}d word is {listt} ")

 


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
 
    shift = shift % 26
    caesar(plain_direction=direction,plain_text=text,plain_shift=shift)

    x = input("Type \"yes\" if you wnat to go again otherwise \"no\"\n")

    if x == "no":
        should_continue = False
        print("Good Bye!")



