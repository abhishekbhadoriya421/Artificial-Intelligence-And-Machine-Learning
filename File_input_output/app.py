def file_name(fileName: str):
    try:
        file = open(fileName, 'r')
        content = file.read()
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print(f"The file {fileName} does not exist.")

fileName = 'data.csv'
file_name(fileName)