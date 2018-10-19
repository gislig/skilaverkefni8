import string

# (1) Type in the document
def open_file_stream():
    try:
        # Allows the user to type in a document name
        filename = input("Document collection: ")
        #filename = "./skilaverkefni8/ap_docs.txt"
        file_string = ""
        # if the file exists then read it into a file_stream
        with open(filename) as file_stream:
            # Set the contents of the file into a variable and close the file
            file_string = file_stream.read()
    except FileNotFoundError:
        file_string = None

    # Return the contents of the variable empty or not
    return file_string

# (2) Select from menu
def menu_selection():
    # Users selection menu
    print("What would you like to do?")
    print("1. Search Documents")
    print("2. Print Document")
    print("3. Quit Program")
    selection = input("> ")
    return selection

# (3) Create a dictionary from the contents of a file
def create_word_dict(text_content):
    word_dict = {}
    # Convert the text content to a list of documents
    document_list = convert_content_to_documents(text_content)
    for index, value in enumerate(document_list):
        # remove returns and split the words based on empty string
        words = value.strip().split()
        for word in words:
            # set the word to lower and remove all the punctiations
            word = word.lower().strip(string.punctuation)
            if word not in word_dict:
                # if the key does not exist, add a new set into a key with the value of index
                word_dict[word] = {index}
            else:
                # if the key exists, append to the set
                word_dict[word].add(index)
                
    return word_dict

# (2.1) Search Documents based on user input
def search_documents(word_dict):
    # User types in search words
    search_list = input("Enter search words: ")
    # Splits the words based on space
    search_list = search_list.split()
    for search_string in search_list:
        if search_string in word_dict:
            # if the word exists as a key in the word_dict then print it out the set
            documents_found = ' '.join(str(n) for n in word_dict[search_string])
            print("Documents that fit search: {}".format(documents_found))
        else:
            # if there is no match to the search then report no match
            print("No match.")

# (2.2) Print out the selection of the document
def print_document_number(text_content):
    # User selects the document number
    select_doc_number = int(input("Enter document number: "))
    document_list = convert_content_to_documents(text_content)
    try:
        document_printout = document_list[select_doc_number]
        print("Documnent #{}{}".format(select_doc_number,document_printout))
    except IndexError:
        # If the document does not exist it will give out an error
        print("Document does not exist.")

# (4) Convert the contents into documents
def convert_content_to_documents(file_contents):
    # Convert the text_content to a multiple documents
    document_list = file_contents.split("<NEW DOCUMENT>")
    return document_list

# Main function
def main():
    text_content = open_file_stream()
    if text_content is None:
        # If the return is none then the document was not found
        print("Documents not found.")
        # returns and exists the program
        return
    else:
        # Creates a dictionary for the text content
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