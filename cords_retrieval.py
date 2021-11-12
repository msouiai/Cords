def process_cords_content(cords_content):
    print("Processing Cord Content")

def read_cords_file(cord_file_name):
    print("Reading the following Cords File")
    print(cord_file_name)
    # Opening file but its not read yet
    file = open(cords_file_name,'r')
    # Reading the file
    # Marcos Magic ***********


def read_cords(cord_file_name):
    print("Reading Cords")
    # We are reading the file here
    cords_content = read_cords_file(cord_file_name)
    # Alright we have the content
    process_cords_content(cords_content)


cords_file_name = "simple_acordes_e_harmonia.txt"
read_cords(cords_file_name)


