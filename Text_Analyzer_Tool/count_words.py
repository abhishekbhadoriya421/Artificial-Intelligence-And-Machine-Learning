
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
        'char_count_without_space': 0
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
    return words