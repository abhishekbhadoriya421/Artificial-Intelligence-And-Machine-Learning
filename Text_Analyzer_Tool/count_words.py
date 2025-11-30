
def get_word(text: str)-> int:
    if(len(text) == 0 or not isinstance(text, str)):
        return 0
    trimed_text = text.strip()
    words = {
        'word_count': 0,
        'words': [],
        'word_frequency': {},
        'unique_words': set(),
        'char_count_with_space': 0,
        'char_count_without_space': 0,
        'most_repeating_word':0,
        'top_5_words':[]
    }
    
    text = trimed_text.lower()
    word = ''
    skip_char = ['.',',','!','?',';',':']
    for char in text:
        words['char_count_with_space'] += 1
        if char != ' ' and char != '\n' and char != '\t' and char != '\r':
            words['char_count_without_space'] += 1
        if (char == ' ' or char == '\n' or char == '\t' or char == '\r') and word != '':
            words['words'].append(word)
            words['unique_words'].add(word)
            words['word_count'] += 1
            if word in words['word_frequency']:
                words['word_frequency'][word] += 1
            else:
                words['word_frequency'][word] = 1
            word = ''
        elif char != ' ' and char != '\n' and char != '\t' and char != '\r' and char not in skip_char:
            word += char
    if word != '':
        words['words'].append(word)
        words['unique_words'].add(word)
        words['word_count'] += 1

    words['word_frequency'] = dict(sorted(words['word_frequency'].items(), key = lambda item: item[1],reverse=True ))
    count = 1
    for key in words['word_frequency'].keys():
        if(count>=6):
            break
        words['top_5_words'].append(key)
        count+=1
    print(words['top_5_words'])


    return words