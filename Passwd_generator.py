import random 
import string

length = int(input("Enter length: "))

LowerLetters=string.ascii_lowercase
UpperLetters = string.ascii_uppercase

Digits = string.digits
Symbols = ['@','#','$','&','%']

List_of_characters=[]
List_of_characters.extend(UpperLetters)
List_of_characters.extend(LowerLetters)
List_of_characters.extend(Digits)
List_of_characters.extend(Symbols)
#print(List_of_characters)

psswd=random.sample(List_of_characters,length)
#print(psswd)

password="".join(psswd)
print(password)
