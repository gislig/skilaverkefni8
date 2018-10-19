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

# (2) Select from menu
def menu_selection():
    print("What would you like to do?")
    print("1. Search Documents")
    print("2. Print Document")
    print("3. Quit Program")
    selection = input("> ")
    return selection

# (2.1) Search Documents eftir viðeigandi orðum út frá bili
def search_documents(doc_list):
    print("Enter search words: stock prices")
    search_list = ["stock","prices"]
    found_in_docs = {}
    for sl in search_list:
        for index, doc in enumerate(doc_list):
            if sl in doc:
                found_in_docs[sl] = index
    print(found_in_docs)

# (2.2) Print out the selection of the document
def print_document_number(doc_list):
    select_doc_number = int(input("Enter document number: "))
    print("Documnent #{}{}".format(select_doc_number,doc_list[select_doc_number]))

# (3) Convert the contents into documents
def convert_content_to_documents(file_contents):
    document_list = file_contents.split("<NEW DOCUMENT>")
    return document_list


# Read Article
def main():
    file_contents = open_file_stream()
    if file_contents is None:
        print("Documents not found.")
        return
    while True:
        document_list = convert_content_to_documents(file_contents)
        selection = menu_selection()
        #selection = 1
        if selection == '1':
            # Search for specific words in the document
            search_documents(document_list)
        if selection == '2':
            # Print out specific documnent number
            print_document_number(document_list)
        if selection == '3':
            # Exits the application
            print("Exiting program.")
            return
main()