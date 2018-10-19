# (1) Type in the document
def open_file_stream():
    try:
        #filename = input("Document collection: ")
        filename = "./skilaverkefni8/ap_docs.txt"
        file_string = ""
        with open(filename) as file_stream:
            file_string = file_stream.read()
    except FileNotFoundError:
        file_string = None
    return file_string

def convert_content_to_documents(file_contents):
    document_list = file_contents.split("<NEW DOCUMENT>")
    return document_list

def remove_punctiations(word):
    pass

def create_word_dict(text_content):
    words_dict = {}

    document_list = convert_content_to_documents(text_content)
    for index, value in enumerate(document_list):
        words = value.split()
        for word in words:
            word = word.lower()
            if word in words_dict:
                words_dict[word] = index
            else:
                words_dict[word] = index

    return words_dict

text_content = open_file_stream()
words = create_word_dict(text_content)
print(words)