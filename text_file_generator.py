def text_file_generator(filename, text):
    with open(f'{filename}.txt', 'w+') as myFile:
        myFile.write(text + '\n')

