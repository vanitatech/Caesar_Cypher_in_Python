import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(original_text, shift_amount, encode_or_decode):
    cypher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            cypher_text += letter
        else:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cypher_text += alphabet[new_position]
    print(f"Here is the {encode_or_decode}d result: {cypher_text}")

only_continue = True

while only_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(original_text = text, shift_amount = shift, encode_or_decode= direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n")
    if restart == "no":
        only_continue == False
        print("Goodbye")

