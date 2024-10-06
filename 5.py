def encrypt_message(message, group_size):
   
    groups = ['' for _ in range(group_size)]
    
   
    for index, char in enumerate(message):
        groups[index % group_size] += char

    
    encrypted_message = ''.join(groups)
    return encrypted_message


user_message = input()
group_size = int(input())


encrypted = encrypt_message(user_message, group_size)


print(encrypted)
