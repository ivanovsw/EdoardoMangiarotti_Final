
#Name: Stefan Ivanov + Justin Jennings
#email: ivanovsw@mail.uc.edu, 
#Assignment Title: Assignment Final
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that I can build an encryption project 
#Citations:
#Anything else that's relevant:


def read_english_text_file(filename):
    with open(filename, 'r') as f:
        english_text = f.readlines()
    return english_text

def decrypt_message(encrypted_values, english_text):
    decrypted_string = ""
    for value in encrypted_values:
        decrypted_string += english_text[int(value)-1].strip() + " "
    return decrypted_string
