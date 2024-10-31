ask = input("Type 'encrypt' for encryption and 'decrypt' for decryption: ")

alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar_cipher(message, shift, mode):
    result = ""

    for char in message:
        if char.isalpha():
            if char.islower():
                alpha = alpha_lower
            else:
                alpha = alpha_upper

            index = alpha.index(char)
            if mode == "encrypt":
                shifted_index = (index + shift) % 26
            elif mode == "decrypt":
                shifted_index = (index - shift) % 26

            result += alpha[shifted_index]
        else:
            result += char

    return result


if ask == "encrypt":
    mess = input("Type your message: ")
    num = int(input("Type shift number: "))
    encrypted_message = caesar_cipher(mess, num, "encrypt")
    print("Encrypted message:", encrypted_message)

elif ask == 'decrypt':
    mess = input("Type your message: ")
    num = int(input("Type shift number: "))
    decrypted_message = caesar_cipher(mess, num, "decrypt")
    print("Decrypted message:", decrypted_message)

else:
    print("Invalid syntax")
input("Press Enter to continue...")
