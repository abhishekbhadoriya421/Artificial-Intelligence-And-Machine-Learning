from read_file import read

def main():
    print("Welcome to the Text Analyzer Tool!")
    try:
        file_path = 'content_file.txt'
        content = read(file_path)
        if content:
            pass
        else:
            print("No content to analyze.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    

if __name__ == "__main__":
    main()