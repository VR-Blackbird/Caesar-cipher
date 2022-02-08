text = input("Enter the Text: \n")
shift = int(input("Enter the shift value\n"))
cipher = ''


def get_cipher(code, order, first):
    if code > ord(order):
        diff = code - ord(order) - 1
        return chr(ord(first) + diff)
    return chr(code)


for word in text:
    if word.isalpha():
        code_point = ord(word)+shift
        if word.isupper():
            cipher += get_cipher(code_point, 'Z', 'A')
        else:
            
            cipher += get_cipher(code_point, 'z', 'a')
    else:
        cipher += word
        
print(cipher)
