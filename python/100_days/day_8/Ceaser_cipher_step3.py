alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def ceaser(input_text, shift_amount, cipher_direction):
    output_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
            output_text += alphabet[new_position]
        elif cipher_direction == "decode":
            new_position = position - shift_amount
            output_text += alphabet[new_position]
        else:
            raise AttributeError('Input can only be encode or decode')
    print(f"The {cipher_direction}d text is {output_text}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceaser(input_text=text, shift_amount=shift, cipher_direction=direction)
