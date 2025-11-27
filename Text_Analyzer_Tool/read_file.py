
def read(file_path: str):
    try:
        file = open(file_path,'r')
        content = file.read()
        file.close()
        return content
    except FileNotFoundError or IOError:
        print(f"The file {file_path} was not found.")
        return False
    