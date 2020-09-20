def text_file_generator(filename, text):

    myfile = open(f'{filename}.txt', "a")
    myfile.write(text + '\n')
    myfile.close()
