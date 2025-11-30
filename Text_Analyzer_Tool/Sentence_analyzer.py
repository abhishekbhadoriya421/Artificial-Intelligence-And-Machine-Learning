
def sentence_analyzer(text: str):
    if(len(text) == 0 or not isinstance(text, str)):
        return 0
    trimed_text = text.strip()
    text = trimed_text.lower()
    sentence = {
        'sentence_count': 0,
        'sentences': [],
    }
    
    sentences = text.split('.') + text.split('!') + text.split('?')
    sentence['sentence_count'] = len([s for s in sentences if(s.strip())])
    sentence['sentences'] = [s for s in sentences if(s.strip())]
    for sentence_text in sentence['sentences']:
        print(f"- {sentence_text.strip()}")  
