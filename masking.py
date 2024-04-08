def mask_func(person):
    masked_person = {}  
    for key in person:
        if key in ['first_name', 'last_name', 'date_of_birth', 'email_address']:  
            word = person[key]
            words = []
            if '@' in word:
                words = word.split('@')
            elif '-' in word:
                words = word.split('-')
            else:
                words = word.split()
            
        
            masked_words = []

            for word in words:
                word_list = list(word)
                for i in range(len(word_list)):
                    if len(word_list) < 3:
                        if i > 0:
                            word_list[i] = '*'  
                        masked_word = ''.join(word_list)
                    else:
                        if i > 1:
                            word_list[i] = '*'  
                        masked_word = ''.join(word_list)
                    

                masked_words.append(masked_word)
                masked_string = '-'.join(masked_words)
                masked_person[key] = masked_string  
        else:
            masked_person[key] = person[key]  

    return masked_person

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'date_of_birth': '1990-05-15',
    'email_address': 'john@mail.com',
}

print(mask_func(person))




