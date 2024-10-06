def match_pattern(strings, pattern):
 
    matches = []
    

    for s in strings:
        if len(s) != len(pattern):
            continue 
        
       
        match = True
        for char_s, char_p in zip(s, pattern):
            if char_p != '*' and char_s != char_p:
                match = False
                break
        
    
        if match:
            matches.append(s)
    
    return matches


L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']


user_input = 'a**a****'


matching_strings = match_pattern(L, user_input)
print(matching_strings)
