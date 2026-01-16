alphabett = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]
direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
text = input("Type you messaage:\n".lower())
shift = input("Type your shifting number:\n")

#todo: create a encrypt function that takes text and shift as input
def encrypt(plain_text,shift_amount):
    #todo2 : inside the function text takes the shift amount and moves it
    cipher=""
    for letter in plain_text:
        position = alphabett.index(letter)
        new_position = position + shift_amount
        new_letter = alphabett[new_position]
        cipher+=new_letter
        
    print(cipher)