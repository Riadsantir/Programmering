import random

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    length = 12
    password = "".join(random.sample(characters, length))
    return password

print("Genererat lösenord:", generate_password())