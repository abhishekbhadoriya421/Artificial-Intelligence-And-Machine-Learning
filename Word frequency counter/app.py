
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
            
    for key,value in words.items():
        print(key,': ',value)
        
        
para = 'I    love     python'


count_word_frequency(para)