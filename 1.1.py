def swap_and_combine(str1, str2):
    
    new_str1 = str2[:2] + str1[2:] 
    new_str2 = str1[:2] + str2[2:]  
   
    result = new_str1 + ' ' + new_str2
    return result


string1 = 'kbtu'
string2 = 'mkm'


result = swap_and_combine(string1, string2)


print(result)
