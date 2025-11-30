
def sentence_analyzer(text: str):
    if(len(text) == 0 or not isinstance(text, str)):
        return 0
    trimed_text = text.strip()
    text = trimed_text.lower()
    sentence = {
        'sentence_count': 0,
        'sentences': [],
    }
    
    sentence_endings = ['.','!','?']
    sentence_count = text.split('.') + text.split('!') + text.split('?')
    