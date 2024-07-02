import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter length of password: "))
    if length <= 0:
        print("length must be greater than zero")
    password = generate_password(length)
    print("generated password is:" + password)



main()

