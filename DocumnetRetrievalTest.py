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

# (2.1) Search Documents letar eftir viðeigandi orðum út frá bili
# (2.2) Prenta út skjalið
# Read Article

def main():
    file_contents = open_file_stream()
    if file_contents is None:
        print("Documents not found.")
        return
    while True:
        selection = menu_selection()
        if selection == '1':
            # Search for specific words in the document
            print("Search Documnets")
        if selection == '2':
            # Print out specific documnent number
            print("Print Documents")
        if selection == '3':
            return
main()