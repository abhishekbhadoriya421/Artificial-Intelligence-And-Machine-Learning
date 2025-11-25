
def count_word_frequency(para: str):
    para = para.strip()
    spliter = [' ',',','.']
    words = {}
    word = ''
    for alpha in range(0,len(para)):
        if para[alpha] in spliter:
            if word == '':
                alpha += 1
                continue
            word = word.lower()
            if word in words:
                words[word] =  words[word]+1
            else:
                words[word] = 1
            word = ''
        else:
            word = word + para[alpha]
    if word != '':
        word = word.lower()
        if word in words:
            words[word] =  words[word]+1
        else:
            words[word] = 1
            
    return words
    
def sort_word_frequency(words: dict):
    sorted_words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))
    return sorted_words
     
para = '     I    love     python because     Python  is easy     and python is powerful      '

words = count_word_frequency(para)
def a(item):
    return item[1]
print("Word Frequency Count:")
print(dict(sorted(words.items(),key= a,reverse=True)))
# print(sort_word_frequency(words))