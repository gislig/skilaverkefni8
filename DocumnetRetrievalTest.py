import string

# (1) Type in the document
def open_file_stream():
    try:
        #filename = input("Document collection: ")
        filename = "./skilaverkefni8/ap_docs2.txt"
        file_string = ""
        with open(filename) as file_stream:
            file_string = file_stream.read()
    except FileNotFoundError:
        file_string = None
    return file_string

def convert_content_to_documents(file_contents):
    document_list = file_contents.split("<NEW DOCUMENT>")
    return document_list

def convert_list_to_Set(word_dict):
    pass

def create_word_dict(text_content):
    word_dict = {}

    document_list = convert_content_to_documents(text_content)
    #for document_index in range(len(document_list)):
    for index, value in enumerate(document_list):
        words = value.strip().split()
        for word in words:
            word = word.lower().strip(string.punctuation)
            if word not in word_dict:
                word_dict[word] = {index}
            else:
                word_dict[word].add(index)
                
    return word_dict

text_content = open_file_stream()
wordings = create_word_dict(text_content)
print(wordings)
