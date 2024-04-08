def mask_func(person):
    masked_person = {}  
    for key in person:
        if key in ['first_name', 'last_name', 'date_of_birth', 'email_address']:  
            word = person[key]
            masked_words = []

            
            word_list = list(word)
            for i in range(len(word_list)):
                if i > 1:
                    word_list[i] = '*'  
            masked_word = ''.join(word_list)
            masked_words.append(masked_word)

            masked_string = ' '.join(masked_words)
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




