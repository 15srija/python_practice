import alphabet

def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if plain_text in alphabet.letters:
         position=alphabet.letters.index(char)
         e=(position+shift_key)%26
         cipher_text+=alphabet.letters[e]
        else:
            cipher_text+=char
    print(f"Here is the text after encyption:\n{cipher_text}")

def decryption(cipher_text,shift_key):
    decrypt_text=""
    for char in cipher_text:
        if cipher_text in alphabet.letters:
            position=alphabet.letters.index(char)
            d=(position-shift_key)%26
            decrypt_text+=alphabet.letters[d]
        else:
            decrypt_text+=char
    print(f"Here is the decrypted message:\n{decrypt_text}")
end=False
while not end:
    what_to_do=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:")
    text=input("Enter the message:")
    key=int(input("Enter the key value:"))
    if what_to_do=='encrypt':
        encryption(plain_text=text,shift_key=key)
    elif what_to_do=='decrypt':
        decryption(cipher_text=text,shift_key=key)
    play_again=input("Type 'yes' to continue, 'no' to end the program:")
    if play_again=='no':
        end=True
        print("Have a nice day! Byee!!..")