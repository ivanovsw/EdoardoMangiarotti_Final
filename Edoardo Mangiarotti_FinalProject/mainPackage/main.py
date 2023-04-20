
#Name: Stefan Ivanov + Justin Jennings
#email: ivanovsw@mail.uc.edu, jenninjx@mail.uc.edu
#Assignment Title: Assignment Final
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that I can build an encryption project 
#Citations: ChatGPT
#Anything else that's relevant:

import json
from PIL import Image
import functionsPackage.functions 

with open('EncryptedGroupHints Spring 2023 Section 001.json', 'r') as f:
    data = json.load(f)

    # print team key values
    for key, value in data.items():
        if key == 'Edoardo Mangiarotti':
            print(key, ":" ,value)

english_text = functionsPackage.functions.read_english_text_file('English.txt')
decrypted_string = functionsPackage.functions.decrypt_message(data["Edoardo Mangiarotti"], english_text)
print(decrypted_string)

# Open image file (we need to replace shaq.png with our pic) 
image = Image.open("GroupPic.jpeg")
image.show()



