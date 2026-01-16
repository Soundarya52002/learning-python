alphabett = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]
#todo: create a encrypt function that takes text and shift as input
#def encrypt(plain_text,shift_amount):
    #todo2 : inside the function text takes the shift amount and moves it
    #cipher = ""
    #for letter in plain_text:
        #position = alphabett.index(letter)
        #new_position = (position + shift_amount)%26
        #new_letter = alphabett[new_position]
        #cipher+=new_letter
        
    #print("Encrypted text:", cipher)
#todo: create a decrypt function that takes text and shift as input
#def decrypt(cipher_text,shift_amount):
    #todo2: inside the function text takes the shift amount and moves it backwards
    #decrypting = ""
    #for letter in cipher_text:
        #position = alphabett.index(letter)
        #new_position = (position - shift_amount)%26
        #new_letter = alphabett[new_position]
        #decrypting+=new_letter
    #print("Encrypted text:", decrypting)

#todo: make a single ceaser function
def ceaser(start_text,shift_amount,direction):
    end_text = ""
    if direction == "decode":
            shift_amount *= -1
#todo what happens if the user use anything other than letters like special character
    for char in start_text:
        if char in alphabett:
            position = alphabett.index(char)
            new_position = (position + shift_amount)%26
            new_letter = alphabett[new_position]
            end_text+= new_letter
        else: 
             end_text+= char
    print(f"The {direction}d text is ",end_text)

#todo ask the user yes if wants to continue giving the text and do the ciphering
# Loop to continue program
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shifting number:\n"))

    ceaser(text, shift, direction)

    result = input("Enter 'yes' to continue or 'no' to stop:\n").lower()
    if result == 'no':
        should_continue = False
        print("Good bye!")




