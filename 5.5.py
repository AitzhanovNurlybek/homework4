def translate_word(word):
    vowels = 'aeiou'
    if word[0].lower() in vowels: 
        return word + 'yay'
    else:
    
        for i in range(len(word)):
            if word[i].lower() in vowels:
                return word[i:] + word[:i] + 'ay'
        
        return word + 'ay'

def translate_sentence(sentence):
    words = sentence.split() 
    translated_words = [translate_word(word) for word in words] 
    return ' '.join(translated_words)


input_text = input()


result = translate_sentence(input_text)

print(result)
