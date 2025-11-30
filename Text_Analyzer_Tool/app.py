from read_file import read
from count_words import get_word
from Sentence_analyzer import sentence_analyzer

def main():
    print("Welcome to the Text Analyzer Tool!")
    try:
        file_path = 'content_file.txt'
        content = read(file_path)
        if content:
            words = dict(get_word(content))
            # print('Word Count: ', words['word_count'])
            # print('Unique Word Count: ', len(words['unique_words']))
            # print('Total Character With Space: ', words['char_count_with_space'])
            # print('Total Character Without Space: ', words['char_count_without_space'])
            # print('\n')
            # print(words['words'])
            # print('\n')
            # print('Unique Words: ', words['unique_words'])
            sentence_analyzer(content)
        else:
            print("No content to analyze.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    

if __name__ == "__main__":
    main()