import string

# (1) Type in the document
def open_file_stream():
    try:
        filename = input("Document collection: ")
        #filename = "./skilaverkefni8/ap_docs.txt"
        file_string = ""
        with open(filename) as file_stream:
            file_string = file_stream.read()
    except FileNotFoundError:
        file_string = None
    return file_string

# (2) Select from menu
def menu_selection():
    print("What would you like to do?")
    print("1. Search Documents")
    print("2. Print Document")
    print("3. Quit Program")
    selection = input("> ")
    return selection

def create_word_dict(text_content):
    word_dict = {}

    document_list = convert_content_to_documents(text_content)
    for index, value in enumerate(document_list):
        words = value.strip().split()
        for word in words:
            word = word.lower().strip(string.punctuation)
            if word not in word_dict:
                word_dict[word] = {index}
            else:
                word_dict[word].add(index)
                
    return word_dict

# (2.1) Search Documents eftir viðeigandi orðum út frá bili
def search_documents(word_dict):
    search_list = input("Enter search words: ")
    search_list = search_list.split()
    for s in search_list:
        if s in word_dict:
            documents_found = ' '.join(str(n) for n in word_dict[s])
            print("Documents that fit search: {}".format(documents_found))
        else:
            print("No match.")
    #print(found_in_docs)

# (2.2) Print out the selection of the document
def print_document_number(text_content):
    select_doc_number = int(input("Enter document number: "))
    document_list = convert_content_to_documents(text_content)
    document_printout = document_list[select_doc_number]
    print("Documnent #{}{}".format(select_doc_number,document_printout))

# (3) Convert the contents into documents
def convert_content_to_documents(file_contents):
    document_list = file_contents.split("<NEW DOCUMENT>")
    return document_list

# Read Article
def main():
    text_content = open_file_stream()
    if text_content is None:
        print("Documents not found.")
        return
    else:
        word_dict = create_word_dict(text_content)
    while True:
        selection = menu_selection()
        if selection == '1':
            # Search for specific words in the document
            search_documents(word_dict)
        if selection == '2':
            # Print out specific documnent number
            print_document_number(text_content)
        if selection == '3':
            # Exits the application
            print("Exiting program.")
            return
main()