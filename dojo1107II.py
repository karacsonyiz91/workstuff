def find_message(text):
    secret_message = ""
    #str_length = len(text)

    for char in text:
        if char.isupper():
            secret_message += char

    return secret_message

print(find_message("Sajtos MakarÓni"))            