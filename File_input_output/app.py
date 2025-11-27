def file_Read(fileName: str):
    try:
        fileRead = open(fileName, 'r')
        content = fileRead.read()
        print("File Content:")
        print(content)
        fileRead.close()
    except FileNotFoundError:
        print(f"The file {fileName} does not exist.")
        
def file_Write(fileName: str, data: str = "Sample data to write to file."):
    try:
        fileWrite = open(fileName, 'w')
        fileWrite.write(data)
        fileWrite.close()
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
      
fileName = 'data.csv'
file_Read(fileName)
file_Write(fileName,'this is empty file now')
file_Read(fileName)